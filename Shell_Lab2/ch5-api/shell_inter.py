#! /usr/bin/env python3

import os, sys, time, re

pid = os.getpid()
rc = os.fork()

if rc < 0:
    sys.exit(1)

elif rc == 0:                   # child
   
    file_out = ''
    file_in = ''
    args = input('>> ') # get command
    if len(args) == 0 :
        sys.exit(1)
    args = re.split('>', args)
    if len(args) == 2:
        file_out = re.split(' ', args[1])
        file_out = file_out[1]
        args = re.split(' ', args[0])
        args = args[:-1]
        os.close(1)
    else:
        args = re.split(' ', args[0])
    if file_out != '':
        sys.stdout = open(file_out, 'w' )
        fd = sys.stdout.fileno()
        os.set_inheritable(fd, True)              
    for dir in re.split(":", os.environ['PATH']): # try each directory in the path
        program = "%s/%s" % (dir, args[0])
        try:
            os.execve(program, args, os.environ) # try to exec program
        except FileNotFoundError:             # ...expected
            pass                              # ...fail quietly

    sys.exit(1)                 # terminate with error

else:                           # parent (forked ok)
    childPidCode = os.wait()
