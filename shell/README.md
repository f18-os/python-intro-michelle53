# Shell in Python

The shell_inter.py program runs a python "script" that takes a two argument
commands and does the function. It implements input redirection (as in using
the argument after < as an argument value in the command before <), output
redirection (as in saving output to a txt file or something else) and pipe (|).

Although efforts were made to consider ps1, it is inconclusive.

The program fails with the give testShell.sh but performs the commands when done manually in the program's shell.

To run the program you need to first do the following:
~~~
python3 shell_inter.py

~~~
To end shell:
~~~
bye
~~~

Some Examples(tested):
~~~
echo hello
wc shell_inter.py > shell_word_count.txt
ls | more
ls | sort
wc -l < myoutput
cd ../
~~~
