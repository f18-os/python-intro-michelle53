#! /usr/bin/env python3

import os, sys, time, re


# execute shell
def execute_shell(args):
    if args[0] == '': # avoids empty arguments that may have been passed
        sys.exit(1)
    elif '/' in args[0]: # means we have a path 
        try:
            os.execve(args[0], args, os.environ)
        except FIleNotFoundError:
            pass
    else: # if we don't have a path then we find the path for the arguemnt
        for dir in re.split(':', os.environ['PATH']):
            program = '%s/%s' % ( dir, args[0] )
            try:
                os.execve(program, args, os.environ)
            except FileNotFoundError:
                pass
    print( 'Command not found' ) # if nothing works then we just print out error


# pipe function 
def pipe(args):
    args = re.split('[|]', args)
    args = [ x.strip(' ') for x in args]
    args[0] = re.split(' ', args[0])    
    read, write = os.pipe()
    rc = os.fork()
    if rc == 0:
        os.close(read)
        os.dup2(write, sys.stdout.fileno()) # write output to the systems output
        os.close(write)
        tmp_a = args[0]
        execute_shell(tmp_a)
        #sys.exit(1)
    else:
        parent_wait = os.wait()
        os.dup2(read, sys.stdin.fileno()) # write the system's output to the system's input
        tmp_a = [args[1]]
        execute_shell(tmp_a)
        sys.exit(1)

# right redirection pipe
def right_redirect(args):
    args = re.split('>', args)
    file_out = args[1].strip() # get the output file
    args = re.split(' ', args[0].strip() ) # get teh input argumnet
    os.close(1)

    sys.stdout = open(file_out, 'w')
    fd = sys.stdout.fileno()
    os.set_inheritable(fd, True)
    execute_shell( args )

# left redirection pipe
def left_redirect(args):
    args = re.split('<', args)
    args = [ x.strip(' ') for x in args ] # what I assume is basically just using 2 command as input
    execute_shell(args)

    

# implement a shell
def shell_implement(args):
   args = args.strip()
   if '|' in args: # a pipe was found
       pipe(args)
   elif '>' in args:
       right_redirect(args)
   elif '<' in args:
       left_redirect(args)
   else:
       args = re.split(' ', args) # a simple command was found
       execute_shell(args)

# forks to implement the shell    
def shell(args):
    rc = os.fork()
    if rc < 0:
        print( 'error in forking: ' + rc )
        sys.exit( 1 )
    elif rc == 0:
        shell_implement( args )
    else:
        childPid = os.wait()

# check ps1
if os.environ['PS1']:
    PS1 = os.environ['PS1']
else:
    PS1 = '$'

try:
    #print(PS1),
    stdin = sys.stdin.readlines()
    for line in stdin:
        if 'cd' in line: # change directories
            directory = re.split(' ', line.strip() ) 
            os.chdir( directory[ 1 ] )
        elif 'exit' in line:
            sys.exit() # exit because we want to exit
        else: # execute coomand
            shell(line.strip())

except EOFError:
    pass
