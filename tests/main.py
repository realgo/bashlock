#!/usr/bin/env python3

import pytest
import os
import random
from bashlock import Bashlock


def find_unused_pid():
    for i in range(100):
        pid = random.randint(2, 32000)
        try:
            os.kill(pid, 0)
        except ProcessLookupError:
            return pid
    raise ValueError('Could not find an unused PID')


def test_basic(tmpdir):
    assert Bashlock(tmpdir + '/lockfile').acquire()
    assert not Bashlock(tmpdir + '/lockfile').acquire()
    assert not Bashlock(tmpdir + '/lockfile').acquire()


def test_existing_lockfile(tmpdir):
    with open(tmpdir + '/lockfile', 'w') as fp:
        fp.write(str(os.getpid()))
    assert not Bashlock(tmpdir + '/lockfile').acquire()


def test_breaking_lock(tmpdir):
    with open(tmpdir + '/lockfile', 'w') as fp:
        fp.write(str(find_unused_pid()))
    assert Bashlock(tmpdir + '/lockfile').acquire()


def test_another_process_has_lock(tmpdir):
    with open(tmpdir + '/lockfile', 'w') as fp:
        fp.write(str(os.getpid()))
    assert not Bashlock(tmpdir + '/lockfile').acquire()
