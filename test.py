#!/usr/bin/env python3
import time
import lrdebug

'''
Because of the modules purpose of putting the process in an interactive
debugger, the testing is hard to automate. This is instead a very simple script
that can be used to check the modules behaviour manually.

The module uses two environment variables: PM_DEBUGGING and USR_DEBUGGING. To
test run this script with each of these variables either unset or set to 1.
Also make sure that you can easily copy the reported PID to another terminal,
perhaps with the command "kill -10 " already typed in.

If USR_DEBUGGING is set (if the script reports its PID), Run "kill -10 <PID>"
from another terminal! You should end up in an interactive debugger, "c" to
continue.

If PM_DEBUGGING is set the process should after a while end up in a post-mortem
debugger (unless left in the "live" debugger mentioned above). The debugger can
be exited with "c" as above or any of the commands you would otherwise use.

Correct results:
USR_DEBUGGING   PM_DEBUGGING  Expected behaviour:
    -               -         Test script should die after 20 s (division by zero).
    +               -         "Live" debugger should be started. Exit with "c", as above.
    -               +         On exit post-mortem debugger should be started, reporting the error mentioned above.
    +               +         Both of these things should happen.
'''

def redirect1():
    return redirect2()

def redirect2():
    return redirect3()

def redirect3():
    return fail()

def fail():
    time.sleep(20)
    return 1/0

redirect1()

