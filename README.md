bashlock Locking Function for bash
==================================
[![Build Status](https://travis-ci.org/realgo/bashlock.png)](https://travis-ci.org/realgo/bashlock)

This is a function that implements a lockfile and exclusive access via
that file.  It's a bash function that manages the lockfile via a trap
and is meant to easily be pulled into code to prevent multiple instances
from running at once.

Another option is to call the script from "run-one" optional package.
However, bashlock can be used without any external dependencies.

Features
--------

   * Uses trap to remove a lockfile on exit of script.  This is one big
     advantage over using "lockfile(1)" within the script.

   * Writes PID to lockfile and detects if locked process has exited.

   * Provides atomic semantics via "ln".

   * Unit tests.

Getting Started
---------------

Copy the "bashlock" function into your code and then call it with a
lockfile name, exit on failure:

    bashlock /var/run/${0##*/}.pid || exit 1
    [Remainder of script code here]

or:

    BASHLOCKFILE=/var/run/${0##*/}.pid
    bashlock || exit 1

Done!

Contact Information
-------------------

Author: Sean Reifschneider <sean+opensource@realgo.com>  
Date: Wed Sep 18, 2013  
License: 2-Clause BSD  
Code/Bugs: https://github.com/realgo/bashlock
