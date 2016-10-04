# breakable
Write your build system in a real programming language.

[![Coverage Status](https://coveralls.io/repos/github/robertdfrench/break/badge.svg?branch=master)](https://coveralls.io/github/robertdfrench/break?branch=master)

## Build Systems are complicated
Autotools and CMake use obscure Macro languages that compile to Makefiles (or, in the case of autotools, it compiles to a bash file that then generates Makefiles). That's all fine except when it comes to *debugging them*. If your build system is other than non-trivial, you will have to debug it at some point, and that's when all the nasty DSL shitwinds will come crashing down in a buildnami tidal wave.

## Using Breakable
Download the latest [breakable.py](https://raw.githubusercontent.com/robertdfrench/break/master/Breakfile.py) and drop it directly into your application. It's LGPL, so feel free to redistribute as part of another project (that is the intended use). Then you write a `Breakfile.py` which exposes a `BreakTasks` class. Each public method on this class is treated as an entrypoint.

If you have defined `clean` and `test` as methods in your BreakTasks class, you can rebuild your project like so:

```bash
$ ./breakable.py -t clean
$ ./breakable.py -t test
```

To list other entrypoints, run `./breakable.py -l`

## Eat your own dogfood
Breakable builds and tests itself. Take a look at the [Breakfile.py](Breakfile.py) in this directory. 
