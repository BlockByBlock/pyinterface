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
# ENQ = 0x01


class Serialport(object):
    """Create a serial port class."""

    def __init__(self, port, baudrate, bytesize, parity, stopbits,
                 timeout):
        """Return port, baudrate."""
        self.serial = serial.Serial(port, baudrate, bytesize, parity,
                                    stopbits, timeout)
        self.busy = 0
        self.buffer = ""  # Flush
        self.readdata = ""  # Flush

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

    def process_rx(self):
        """Process receiving data."""
        pass

    def writer(self, cmd):
        """Send command."""
        # buffer = ENQ
        self.busy = 1

    def reader(self):
        """Read serial port."""
#        try:
#            while self.alive:
#                data = self.serial.read(1)
#                self.buffer += data
#                rxlen = len(self.buffer)
#                if (rxlen == 1 and self.buffer[0] == chr(STX)):
#                    print "Message received"
#                    self.serial.write(chr(ENQ))
#                    self.buffer = ""  # Flush
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
    session = 1

    try:
        sp = Serialport(port, baudrate, bytesize, parity, stopbits, timeout)
    except serial.SerialException, e:
        sys.stderr.write("Port cannot be open %r: %s\n" % (port, e))
        sys.exit(1)

    sys.stderr.write(' Reading port on %s : %d\n' % (
        sp.serial.port,
        sp.serial.baudrate
    ))

    sp.start()

    print "Reader/Writer Tool for RS232 Device"
    print "Option :: "
    print "1. Write Command"
    print "2. Read Only"
    print "0. Exit"
    print "\n"

    while session == 1:
        cmdkey = raw_input("Number Only. Command: ")
        if cmdkey == "0":
            session = 0
            sp.stop()
        elif cmdkey == "1":
            print "Write Command and send via serial port "
        elif cmdkey == "2":
            print "Read from serial port "
        else:
            print "Reader/Writer Tool for RS232 Device"
            print "Option :: "
            print "1. Write Command"
            print "2. Read Only"
            print "0. Exit"
            print "\n"

    try:
        sp.join()
    except KeyboardInterrupt:
        pass
    sys.stderr.write("\n >>> Exiting... ")
    sp.join()


if __name__ == '__main__':
    main(sys.argv[1:])  # Take all arguments after 1st
