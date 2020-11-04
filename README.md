bashlock Locking Function for bash
==================================
[![Build Status](https://travis-ci.org/solarkennedy/bashlock.png)](https://travis-ci.org/solarkennedy/bashlock)

This includes both a bash function and Python class that implements
exclusive locking via a filesystem file.

This is used to prevent multiple instances of a script from running at the 
same time.

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

Bash:

```bash
bashlock /var/run/${0##*/}.pid || exit 1

# [Remainder of script code here]
```

Python:

```python
from bashlock import Bashlock
if not Bashlock('/tmp/locktest').acquire():
    print('Unable to obtain lock')
    sys.exit(1)

# [Remainder of code here]
```

Done!

Contact Information
-------------------

Author: Sean Reifschneider <sean+opensource@realgo.com>  
Date: Wed Sep 18, 2013  
License: 2-Clause BSD  
Code/Bugs: https://github.com/realgo/bashlock
