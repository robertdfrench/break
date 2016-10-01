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
        cls._print(msg, '==> ', cls.yellow)


class Executable(object):
    def __init__(self, path, defaults=[]):
        self.path = path
        self.defaults = defaults

    def _generate_command(self, *args):
        return ' '.join([self.path] + self.defaults + list(args))

    def __call__(self, argstring=""):
        command = self._generate_command(argstring)
        log.info(command)
        real_command = shlex.split("bash -c '%s'" % command)
        rc = subprocess.call(real_command)
        if rc != 0:  # pragma: no cover
            sys.exit(rc)


def which(tool, defaults=[]):
    paths = ["."] + os.environ['PATH'].split(':')
    for path in paths:
        tool_path = os.path.join(path, tool)
        if os.path.exists(tool_path):
            return Executable(tool_path, defaults=defaults)

rm = which("rm", defaults=["-f"])


def _get_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-l", "--list-tasks",
        help="display available tasks", action="store_true")
    parser.add_argument(
        "-f", "--breakfile",
        help="path to Breakfile.py", default="Breakfile.py")
    parser.add_argument(
        "-t", "--task",
        help="Entrypoint in Breakfile.py", default=None)
    return parser.parse_args(argv)


class RuleCollection(object):
    def __init__(self):
        self.internal_storage = {}
        self.default = None

    def __getitem__(self, key):
        return self.internal_storage[key]

    def __setitem__(self, key, value):
        if not self.default:
            self.default = key
        self.internal_storage[key] = value

    def __str__(self):
        strings = ["Entrypoints:"]
        for k in sorted(self.internal_storage):
            v = self.internal_storage[k]
            strings.append("  %s: %s" % (k, v))
        return "\n".join(strings)

_bk_entrypoints = RuleCollection()


def entrypoint(func):
    _bk_entrypoints[func.__name__] = func.__doc__
    return func

__all__ = ['entrypoint', '_bk_entrypoints', 'which', 'Executable', 'rm']
if __name__ == "__main__":  # pragma: no cover
    args = _get_args(sys.argv[1:])
    import Breakfile as bf
    if args.list_tasks:
        print(bf._bk_entrypoints)
    else:
        if args.task:
            getattr(bf, args.task)()
        else:
            getattr(bf, bf._bk_entrypoints.default)()
