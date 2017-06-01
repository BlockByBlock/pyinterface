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
print "You have send " + cmd + " to serial port\n"
if cmd is not None:
    try:
        ser.write(cmd)
        sleep(1)  # Delay
        response = ser.readline()
        sleep(1)
        response_two = ser.readline()
        sleep(1)
        response_three = ser.readline()
        print response
        print response_two
        print response_three
        ser.close()
    except Exception, ew:
        print ("Error: ") + str(ew)
else:
    print "Exiting"
    sys.exit()
