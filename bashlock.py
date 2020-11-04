#!/usr/bin/env python3
#  vim: ts=4 sw=4 ai et
#
#  Python version of "bashlock" Lockfile managing code.

# Author: Sean Reifschneider <sean+opensource@realgo.com>
# Date: Wed Nov 04, 2020
# License: 2-Clause BSD
# Code/Bugs: https://github.com/realgo/bashlock
#
# This is a Python version of the "bashlock" bash locking function.
# It isn't a literal translation, but it is compatible.
#
# The lock file is managed via an "atexit" to automatically remove
# when the process exits.
#
# Getting Started
# ---------------
#
#   from bashlock import Bashlock
#   if not Bashlock('/tmp/locktest').acquire():
#       print('Unable to obtain lock')
#       sys.exit(1)
#
#   [Remainder of code here]
#
# Done!


class Bashlock:
    def __init__(self, lockfile):
        self.lockfile = lockfile
        self.locked = False

    def acquire(self, try_to_break=True):
        from tempfile import NamedTemporaryFile
        import os
        import atexit

        lockdir, lockprefix = os.path.split(self.lockfile)
        if not lockdir:
            lockdir = '.'

        with NamedTemporaryFile(
                mode='w', prefix=lockprefix + '.', dir=lockdir,
                suffix='.lock') as fp:
            fp.write(str(os.getpid()))
            fp.flush()
            try:
                os.link(fp.name, self.lockfile)
                self.locked = True
                atexit.register(os.remove, self.lockfile)
            except OSError:
                if try_to_break:
                    self._break_lock()

        return self.locked

    def _break_lock(self):
        with open(self.lockfile, 'r') as fp:
            int(fp.readline().strip())
        self.acquire(try_to_break=False)
