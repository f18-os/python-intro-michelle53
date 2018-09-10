#! /usr/bin/env python3

import os, sys, time, re

pid = os.getpid()
rc = os.fork()

if rc < 0:
    sys.exit(1)

elif rc == 0:                   # child
    args = input('>> ') # get command
    if len(args) == 0 :
        sys.exit(1)
    args = re.split(' ', args)
    for dir in re.split(":", os.environ['PATH']): # try each directory in the path
        program = "%s/%s" % (dir, args[0])
        try:
            os.execve(program, args, os.environ) # try to exec program
        except FileNotFoundError:             # ...expected
            pass                              # ...fail quietly

    sys.exit(1)                 # terminate with error

else:                           # parent (forked ok)
    childPidCode = os.wait()
