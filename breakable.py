#!/usr/bin/env python
""" Break: For when you're frustrated with Make.
    Inspired by the elegant process invocation and management features of
    Spack (https://github.com/LLNL/spack).
"""


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

if __name__ == "__main__":
    print("Give me something to break!")
