#!/usr/bin/python

"""
pywrite.

~~~~~~~~~~
This module writes to serial using python.
"""
from openport import open_port
from time import sleep
import sys

ser = open_port(None)

cmd = raw_input("Send Command? >> ")
print "You have send " + cmd + " to serial port"
if cmd is not None:
    ser.write(cmd)
    sleep(.1)
else:
    print "Exiting"
    sys.exit()
