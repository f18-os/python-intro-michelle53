#! /usr/bin/env python3

import os, sys, time, re



# execute commands
def execute_shell(args):
    
    for dir in re.split(":", os.environ['PATH']): # try each directory in the path
        program = "%s/%s" % (dir, args[0])
        try:
            os.execve(program, args, os.environ) # try to exec program
        except FileNotFoundError:             # ...expected
            pass                              # ...fail quietly
    print("Command not found")


# main pipe
def pipe(args):
    args = re.split('[|]', args)
    args[0] = args[0].lstrip(' ')
    args[0] = args[0].rstrip(' ')
    args[1] = args[1].lstrip(' ')
    args[1] = args[1].rstrip(' ')
    
    read, write = os.pipe()
    rc = os.fork()

    if rc == 0: # child
        os.close(read)
        os.dup2(write, sys.stdout.fileno()) # send the output to the standard output
        os.close(write)
        # execute
        tmp_a = [args[0]]

        execute_shell(( tmp_a ) )
        sys.exit(0)

        
    else: # parent

        parent_wait = os.wait()
        os.dup2(read, sys.stdin.fileno())
        
        #execute
        tmp_a = [args[1]]
        execute_shell( ( tmp_a ) )
        sys.exit(1)
        
        

# shell code
def shell_implement(args):
    file_out = '' # file to write to
    
    r_direct = False # check if output redirection
    l_direct = False # check if input redirection
    p_pipe   = False # check if output of first part needed for pipe
    if '>' in args: # right redirection
        r_direct = True
    elif '<' in args: # left redirection
        l_direct = True
    elif '|' in args:
        p_pipe = True
    temp = re.split('[><|]', args) # split
   
    if len(temp) == 2: # if there is redirection
        if r_direct == True: # output redirection
            args = re.split('>', args) # split
            file_out = re.split(' ', args[1])
            file_out = file_out[1]
            args = re.split(' ', args[0])
            args = args[:-1]
            os.close(1)
        elif l_direct == True: # input redirection
            args = re.split('<', args) # split
            file_in = re.split(' ', args[1])
            file_in = file_in[1]
            args = re.split(' ', args[0])
            args = args[:-1]
            args.append(file_in)
            execute_shell(args)
        elif p_pipe == True: # pipe
            pipe(args)
    else: # no redirection
        args = re.split(' ', args)
        execute_shell(args)
    if file_out != '': # set file to be written to as output
        sys.stdout = open(file_out, 'w' )
        fd = sys.stdout.fileno()
        os.set_inheritable(fd, True) 
        execute_shell(args)
    
if __name__ == '__main__':
    continue_fork = True
  
    while(continue_fork):
        args = ''
        if continue_fork == True:
            args = input('$ ')
            if args == 'bye' or args == '':
                continue_fork == False
                sys.exit(1)
            if 'cd' in args:
                args = re.split(' ', args)
                os.chdir(args[1])

        rc = os.fork()
        if rc < 0:
            print("wrong command")
            sys.exit(1)
    
        elif rc == 0: # child
            if args != 'die' and ('cd' in args) == False:
                shell_implement(args)
            sys.exit(1)                # terminate with error
            
        else:                           # parent (forked ok)
            childPidCode = os.wait()



            
