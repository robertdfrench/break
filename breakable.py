#!/usr/bin/env python
""" Break: For when you're frustrated with Make.
    Inspired by the elegant process invocation and management features of
    Spack (https://github.com/LLNL/spack).
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import subprocess
import shlex
import os
import argparse
import sys
import re


class log(object):
    red = '1;31'
    blue = '1;34'
    yellow = '1;33'
    gray = '1;30'

    @classmethod
    def _print(cls, msg, prefix=None, color=None):
        if color:
            msg = "\033[{0}m{1}\033[0m".format(color, msg)
        if prefix:
            msg = prefix + msg
        print(msg)

    @classmethod
    def info(cls, msg):
        cls._print(msg, '# ', cls.yellow)

    @classmethod
    def prompt(cls, msg):
        cls._print(msg, '==> ', cls.blue)


class Executable(object):
    def __init__(self, path, defaults=[]):
        self.path = path
        self.defaults = defaults

    def _generate_command(self, *args):
        return ' '.join([self.path] + self.defaults + list(args))

    def __call__(self, argstring=""):
        command = self._generate_command(argstring)
        log.prompt(command)
        real_command = shlex.split("bash -c \"%s\"" % command)
        rc = subprocess.call(real_command)
        if rc != 0:  # pragma: no cover
            sys.exit(rc)

    def collect(self, argstring):
        command = self._generate_command(argstring)
        log.info(command)
        real_command = shlex.split("bash -c \"%s\"" % command)
        proc = subprocess.Popen(
            real_command,
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1)
        for line in proc.stdout:
            yield line
        rc = proc.wait()
        if rc != 0:  # pragma: no cover
            sys.exit(rc)

    def grab(self, argstring):
        return ''.join(self.collect(argstring))


def which(tool, defaults=[]):
    paths = ["."] + os.environ['PATH'].split(':')
    for path in paths:
        tool_path = os.path.join(path, tool)
        if os.path.exists(tool_path):
            return Executable(tool_path, defaults=defaults)

rm = which("rm", defaults=["-f"])
touch = which("touch")


def find_files(pattern, directory="."):
    for root, dirs, files in os.walk(directory):
        for f in files:
            path = os.path.join(root, f)
            if re.match(pattern, path):
                yield path


def _get_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--list-tasks",
        help="display available tasks", action="store_true")
    parser.add_argument(
        "-c", "--clean",
        help="Clean up breakstamps", action="store_true")
    parser.add_argument(
        "-f", "--breakfile",
        help="path to Breakfile.py", default="Breakfile.py")
    parser.add_argument(
        "-t", "--task",
        help="Entrypoint in Breakfile.py", default=None)
    return parser.parse_args(argv)


def needs(*filenames):
    for f in filenames:
        if not os.path.exists(f):
            raise Exception("%s is needed but not found" % f)


def only_if_modified(*filenames):
    needs(*(filenames + (__file__,)))

    def wrapper(func):
        def wrapped(self=None):
            timestamp_file = path(".breakstamp.%s" % func.__name__)
            dirty = False
            for f in filenames:
                if timestamp_file.dirtier_than(f):
                    dirty = True
                    break
            if dirty:
                of_the_jedi = func(self)
                touch(timestamp_file)
                return of_the_jedi
        wrapped.__doc__ = func.__doc__
        return wrapped
    return wrapper


def provides(filename):
    def wrapper(func):
        def wrapped(self=None):
            if not path(filename).exists:
                return func(self)
        wrapped.__doc__ = func.__doc__
        return wrapped
    return wrapper


class BreakPath(str):
    def newer_than(self, other):
        if not os.path.exists(self):
            msg = "Cannot compare %s with %s." % (self, other)
            msg += " %s does not exist." % (self)
            raise Exception(msg)
        if not os.path.exists(other):
            msg = "Cannot compare %s with %s." % (self, other)
            msg += " %s does not exist." % (other)
            raise Exception(msg)
        return os.path.getmtime(self) > os.path.getmtime(other)

    def dirtier_than(self, dependency):
        if not os.path.exists(dependency):
            msg = "Cannot compare %s with %s." % (self, dependency)
            msg += " %s does not exist." % (dependency)
            raise Exception(msg)
        if not os.path.exists(self):
            return True
        return path(dependency).newer_than(self)

    @property
    def exists(self):
        return os.path.exists(self)


def path(*filename_parts):
    return BreakPath(os.path.join(*filename_parts))

__all__ = [
    'which', 'Executable', 'rm', 'needs', 'find_files', 'path', 'touch',
    'only_if_modified', 'provides', 'log']
if __name__ == "__main__":  # pragma: no cover
    args = _get_args(sys.argv[1:])
    if args.clean:
        for f in find_files(r".*breakstamp.*", "."):
            rm(f)
    from Breakfile import BreakTasks
    tasklist = BreakTasks()
    if args.list_tasks:
        for attr in dir(tasklist):
            if not attr.startswith('_'):
                typename = type(getattr(tasklist, attr)).__name__
                docs = getattr(tasklist, attr).__doc__
                if typename == 'instancemethod':
                    print("%s: %s" % (attr, docs))
    else:
        if args.task:
            getattr(tasklist, args.task)()
        else:
            print("You should probably specify a task")
