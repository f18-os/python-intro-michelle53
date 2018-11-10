# Shell in Python

The shell2.py program runs a python "script" that takes argument
commands and does the function. It implements input redirection (as in using
the argument after < as an argument value in the command before <), output
redirection (as in saving output to a txt file or something else) and pipe (|).

shell2.py is the version that should take into consideration the testSHell and
has some updates to make it cleaner and to take into consideration most guidelines.


The program passes all the tests except those with multiple pipes and that
bash < /tmp/c1 &. All others are accounted for and uncommented in the
testShell.sh file.

To run the program you need to first do the following:
~~~
python3 shell2.py

~~~

To run the testShell.sh along this:
~~~
./testShell.sh ./shell2.py
~~~
To end shell:
~~~
exit
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
