# keylogger
Module to log keystrokes on a remote machine and email to a specified username

Requirements:

[+]  Python 2 and above

[+]  Pynput (pip install pynput)

Usage:

import the module (import keylogger)

Create an instance of the object: klogger = Keylogger([interval], [Gmail username], [Gmail password], [Email to send to])

Call the start method for the object: klogger.start()

Call the program

To terminate logging keystrokes: killall python
