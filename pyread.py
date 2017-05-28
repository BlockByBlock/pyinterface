#!/usr/bin/python

import serial
import time

# Open serial port
ser = serial.Serial(
    # /dev/ttyS1
    # /dev/ttyUSB0
    port = '/dev/ttyUSB0',
    # baudrate: 9600, 14400, 19200, 57600, 115200
    baudrate = 9600,
    # parity: PARITY_ODD, PARITY_EVEN, PARITY_NONE
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHGTBITS,
    # Timeout values:
    # 1. None: wait forever, block call
    # 2. 0: Non-blocking mode, return immediately
    # 3. x, x is bigger than 0, float allowed, timeout blockcall
    timeout = 1 ,
    # Disable - False
    # Software Flow Control
    xonxoff = False,
    # Hardware Flow Control, RTS/CTS
    rtscts = False,
    # Hardware Flow Control, DSR/DTR
    dsrdtr = False,
    # Timeout for write
    writeTimeout = 2
)

try:
    ser.open()
except Exception, e:
    print "error opening serial port: " + str(e)
    exit()

if ser.isOpen()
    try:
        ser.flushInput() #flush input buffer, discarding all contents
        ser.flushOutput() #flush output buffer, abort and discard current output

        
