#!/usr/bin/python

"""
pywrite.

~~~~~~~~~~
This module writes to serial using python.
"""

import serial

config_file = open("portconfig.txt")
cport = config_file.readline().rstrip('\n')
cbaudrate = config_file.readline()

# Open serial port
ser = serial.Serial(
    port=cport,  # Set serial port
    baudrate=cbaudrate,  # baudrate: 9600, 14400, 19200, 57600, 115200
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=0,
    xonxoff=False,
    rtscts=False,
    dsrdtr=False,
    write_timeout=0
)
