#!/usr/bin/env python
""" Break: For when you're frustrated with Make.
    Inspired by the elegant process invocation and management features of
    Spack (https://github.com/LLNL/spack).
"""
import subprocess
import shlex


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


class StringView(object):
    def __init__(self, file_ish):
        self.file_ish = file_ish

    def __str__(self):
        return self.file_ish.read()

    def __iter__(self):
        return self.file_ish


class Executable(object):
    def __init__(self, path, defaults=[]):
        self.cmd = ' '.join([path] + defaults)

    def __call__(self, *args):
        proc = subprocess.Popen(
            shlex.split(self.cmd),
            stderr=subprocess.STDOUT,
            stdout=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1)
        return StringView(proc.stdout)
