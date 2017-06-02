#!/usr/bin/python

"""
pyintf.

~~~~~~~~~~
This module reads from serial using python.
It launches a session to provide a GUI-like option.
-- ybingcheng@gmail.com
"""

import sys
import serial
import threading
import logging
from time import sleep

# STX = 0x02
# ENQ = 0x01

logging.basicConfig(
    filename='serial.log',
    filemode='w',
    format='',
    level=logging.DEBUG
)


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
        cmd = raw_input("Send Command >> ")
        print "Sending" + cmd
        if cmd is not None:
            try:
                self.serial.write(cmd)
                self.busy = 1
                sleep(1)
                response = self.serial.readline()
                sleep(1)
                response_two = self.serial.readline()
                sleep(1)
                response_three = self.serial.readline()
                print response
                print response_two
                print response_three
                self.busy = 0
                self.serial.close()
            except Exception, ew:
                print ("Error: ") + str(ew)

    def reader(self):
        """Read serial port."""
        try:
            while self.serial.isOpen():
                counter = 1  # Read all ASCII
                counter += 1
                self.serial.write(str(chr(counter)))
                sleep(.1)
                if counter == 225:
                    counter = counter  # Reset counter
                dataread = self.serial.readline()
                logging.info(dataread)
                print dataread
        except serial.SerialException, e:
            self.alive = False
            print ("Error: ") + str(e)


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
            sp.reader()
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
