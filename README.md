# lrdebug
Debugging for long running python programs

If you run python code that has a tendency to fail or lock up, but only after a long and/or unpredictable period of time, this module might be able to help you. It enables you to get into the debugger at any time and to automatically get post-mortem debugging should your code exit abnormally.

It's as easy as importing the module and setting (to 1) two environment variables (USR_DEBUGGING and PM_DEBUGGING) and your code should have these capabilities whenever they are needed. Without the environment variables set the module has zero overhead and can safely be left in place for future use.

This module shouldn't interfere with almost anything. However, conflicts might conceivably be possible with code that uses the 'USR1'-signal mechanism or that depends on the state of the top level system exceptionhook.
