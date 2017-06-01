#!/usr/bin/python

"""
openport.

~~~~~~~~~~
This module opens the serial port based on portconfig text file.
"""

import serial
RED = '\033[41m'
GRN = '\033[32m'
WHT = '\033[0m'


def open_port(ser):
    """Open serial port."""
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

    try:
        ser.isOpen()
        ser.reset_input_buffer()
        print GRN + "\n\nPort opened on:" + str(ser.port)
        print "\nBaudrate @ " + str(ser.baudrate) + WHT
    except Exception, e:
        print RED + "Port not open! Error: " + str(e)
        exit()

    return ser
