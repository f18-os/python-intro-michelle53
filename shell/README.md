# Shell in Python

The shell_inter.py program runs a python "script" that takes a two argument
commands and does the function. It implements input redirection (as in using
the argument after < as an argument value in the command before <), output
redirection (as in saving output to a txt file or something else) and pipe (|).

To run the program you need to first do the following:
~~~
python3 shell_inter.py

~~~
To end shell:
~~~
die
~~~

Some Examples(tested):
~~~
echo hello
wc shell_inter.py > shell_word_count,txt
ls -l | more
wc -l < myoutput
~~~
