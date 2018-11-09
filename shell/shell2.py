#! /usr/bin/env python3

import os, sys, time, re


# execute shell
def execute_shell(args):
    if 'cd' in args[0]:
        #new_directory = re.split(' ', args)
        os.chdir( args[1] )
        return
    elif '/' in args[0]:
        try:
            os.execve(args[0], args, os.environ)
            
        except FIleNotFoundError:
            pass
    else:
        for dir in re.split(':', os.environ['PATH']):
            program = '%s/%s' % ( dir, args[0] )
            try:
                os.execve(program, args, os.environ)
            except FileNotFoundError:
                pass
    print( 'Command not found' )



def pipe(args):
    args = re.split('[|]', args)
    args = [ x.strip(' ') for x in args]
    args[0] = re.split(' ', args[0])
    
    read, write = os.pipe()
    rc = os.fork()

    if rc == 0:
        os.close(read)
        os.dup2(write, sys.stdout.fileno())
        os.close(write)
        tmp_a = args[0]
        execute_shell(tmp_a)
        sys.exit(1)
    else:
        parent_wait = os.wait()
        os.dup2(read, sys.stdin.fileno())
        tmp_a = [args[1]]
        execute_shell(tmp_a)
        sys.exit(1)

    
# implement a shell
def shell_implement(args):
   args = args.strip()
   if '|' in args:
       pipe(args)
   else:
       args = re.split(' ', args)
       execute_shell(args)


# check ps1
try:
    PS1 = os.environ['PS1']
except:
    PS1 = '$'

try:
    args = input( PS1 )    
    rc = os.fork()
    if rc == 0:
        shell_implement(args)
    else:
        childPid = os.wait()
except EOFError:
    pass
