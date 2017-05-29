#!/usr/bin/python

import serial
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
    write_timeout=1
)

counter = 32  # Below 32 everything in ASCII is gibberish
while True:
    counter += 1
    ser.write(str(chr(counter)))
    print ser.readline()
    sleep(.1)
    if counter == 255:
        counter = 32
