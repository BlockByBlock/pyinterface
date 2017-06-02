#!/usr/bin/python

"""
pyintf.

~~~~~~~~~~
This module reads from serial using python.
It launches a session to provide a GUI-like option.
-- ybingcheng@gmail.com
"""

import sys
import os
import serial
import threading

# STX = 0x02
# ENQ = SNDA<CR>

class Serialport(object):
    """Create a serial port class."""

    def __init__(self, port, baudrate, bytesize, parity, stopbits,
                 timeout):
        """Return port, baudrate."""
        self.serial = serial.Serial(port, baudrate, bytesize, parity,
                                    stopbits, timeout)
        self.in_cmd = 0

    def start(self):
        """Start serial port thread."""
        self.alive = True
        self.receiver_thread = threading.Thread(target=self.reader)
        self.receiver_thread.setDaemon(True)
        self.receiver_thread.start()

    def stop(self):
        """Close serial port."""
        self.serial.close()
        self.alive = False

    def join(self):
        """Join thread."""
        self.receiver_thread.join()

    def reader(self):
        """Read serial port."""
#        try:
#            while self.alive:
#                data = self.serial.read(1)
#                self.buffer += data
#                rxlen = len(self.buffer)
#                if (rxlen == 1 and self.buffer[0] == chr(STX)
#                   and self.in_cmd == 1):
#                    print "Message received"
#                    self.serial.write(chr(ENQ))
#                    self.in_cmd = 0
#                    self.buffer = ser.reset_input_buffer
#                sys.stdout.flush()
#        except serial.SerialException, e:
#            self.alive = False
#            raise


def main(argv):
    """Open serial port."""
    config_file = open("portconfig.txt")
    port = config_file.readline().rstrip('\n')
    baudrate = config_file.readline()
    bytesize = serial.EIGHTBITS
    parity = serial.PARITY_NONE
    stopbits = serial.STOPBITS_ONE
    timeout = 0
    try:
        sp = Serialport(port, baudrate, bytesize, parity, stopbits, timeout)
    except serial.SerialException, e:
        sys.stderr.write("Port cannot be open %r: %s\n" % (port, e))
        sys.exit(1)

    sys.stderr.write(' Reading port on %s : %d\n' % (
        sp.serial.port,
        sp.serial.baudrate
    ))
