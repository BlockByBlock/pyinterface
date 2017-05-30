#!/usr/bin/python

import serial
import logging
from time import sleep

# Open serial port
ser = serial.Serial(
    port="/dev/ttyUSB0",  # Set serial port
    baudrate=9600,  # baudrate: 9600, 14400, 19200, 57600, 115200
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=0,
    xonxoff=False,
    rtscts=False,
    dsrdtr=False,
    write_timeout=0
)

logging.basicConfig(
    filename='serial.log',
    filemode='w',
    format='',
    level=logging.DEBUG
)

try:
    ser.isOpen()
    print "\n\nPort opened on:" + str(ser.port)
    print "\nBaudrate @ " + str(ser.baudrate)
except Exception, e:
    print "Port not open! Error: " + str(e)
    exit()


def counter_write(counter):
    """Get data from serial via counter."""
    counter += 1
    ser.write(str(chr(counter)))  # convert to string
    sleep(.1)
    if counter == 255:
        counter = counter  # restart counter when reach end
    return counter


if ser.isOpen():
    try:
        ser.reset_input_buffer()
        ser.reset_output_buffer()
        while True:
            counter_write(32)  # Below 32 for ASCII is nonsense
            readData = ser.readline()
            logging.info(readData)
            print readData
    except Exception, e1:
        print ("Error: ") + str(e1)
else:
    print ("Cannot open serial port ")
