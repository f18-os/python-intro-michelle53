#! /usr/bin/env python3

import os, sys, time, re



# shell code
def shell_implement(args):
    file_out = '' # file to write to
    
    r_direct = False # check if output redirection
    l_direct = False # check if input redirection
    if '>' in args: # right redirection
        r_direct = True
    elif '<' in args: # left redirection
        l_direct = True
    args = re.split('[><]', args) # split
    if len(args) == 2: # if there is redirection
        if r_direct == True: # output redirection
            file_out = re.split(' ', args[1])
            file_out = file_out[1]
            args = re.split(' ', args[0])
            args = args[:-1]
            os.close(1)
        elif l_direct == True: # input redirection
            file_in = re.split(' ', args[1])
            file_in = file_in[1]
            args = re.split(' ', args[0])
            args = args[:-1]
            args.append(file_in)
    else: # no redirection
        args = re.split(' ', args[0])            
    if file_out != '': # set file to be written to as output
        sys.stdout = open(file_out, 'w' )
        fd = sys.stdout.fileno()
        os.set_inheritable(fd, True)              
    for dir in re.split(":", os.environ['PATH']): # try each directory in the path
        program = "%s/%s" % (dir, args[0])
        try:
            os.execve(program, args, os.environ) # try to exec program
        except FileNotFoundError:             # ...expected
            pass                              # ...fail quietly
    
if __name__ == '__main__':
    continue_fork = True
  
    while(continue_fork):
        args = ''
        if continue_fork == True:
            args = input('>>')
            if args == 'die' or args == '':
                continue_fork == False
                sys.exit(1)
    
        rc = os.fork()
        if rc < 0:
            sys.exit(1)
    
        elif rc == 0: # child
            if args != 'die':
                shell_implement(args)
            sys.exit(1)                # terminate with error
            
        else:                           # parent (forked ok)
            childPidCode = os.wait()



            
