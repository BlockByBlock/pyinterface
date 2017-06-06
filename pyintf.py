#!/usr/bin/python

"""
pyintf.

~~~~~~~~~~
This module reads from serial using python.
It launches a session and provide a menu option.
-- ybingcheng@gmail.com
"""

import sys
import serial
# import threading
import logging
from time import sleep
from pycolor import WHT, HRED, GRN, BLU, HYEL
from misca import msglength, procfieldvar, procprevfield

# STX = 0x02
# ENQ = 0x01

logging.basicConfig(
    filename='serial.log',
    filemode='w',
    format='',
    level=logging.DEBUG
)


class SerialPort(object):
    """Create a serial port class."""

    def __init__(self, port, baudrate, bytesize, parity, stopbits,
                 timeout):
        """Return port, baudrate."""
        self.serial = serial.Serial(port, baudrate, bytesize, parity,
                                    stopbits, timeout)
        self.dataread = ""  # Flush

#    def start(self):
#        """Start serial port thread."""
#        self.alive = True
#        self.thread = threading.Thread(target=self.listener)
#        # self.thread.setDaemon(True)
#        self.thread.start()

#    def listener(self):
#        """Listen to the serial port."""
#        pass

    def stop(self):
        """Close serial port."""
        self.serial.close()
        print "Exiting...\n"
        sys.exit()
#        self.alive = False

#    def join(self):
#        """Join thread."""
#        self.thread.join()

    def portconfig(self):
        """Configure serial port settings."""
        config_file = open("portconfig.txt", "w")
        cport = raw_input("Set port (e.g. /dev/ttyUSB0) :: ")
        config_file.write(cport)
        print ("Port is configured as " + cport)
        config_file.write("\n")
        cbaudrate = raw_input("Set baudrate (e.g. 9600, 57600, 115200) :: ")
        config_file.write(cbaudrate)
        print ("Baudrate is configured as " + cbaudrate)

        # config_file.close()
        print GRN + "\nPort configured successful and saved!" + WHT
        self.menu()

    def writer(self):
        """Send command."""
        # buffer = ENQ
        store_buffer = ""
        cmd = raw_input("Send Command >> ")
        print "Sending " + HYEL + cmd + WHT
        self.serial.write(cmd)
        sleep(1)  # buffer
        count = 1
        while (count < 5):
            self.dataread = self.serial.readline()
            if (self.dataread.isalnum() is False):
                print self.dataread
                count += 1
                sleep(1)
            else:
                datalen = len(self.dataread)
                if (datalen == msglength):
                    store_msg = self.dataread
                    # print "Msg identified :: "
                else:
                    store_msg = self.dataread
                    store_buffer += store_msg  # store up
                    store_msg = store_buffer
                logging.info(self.dataread)
                print self.dataread
                # print "The msg length is " + str(datalen)
        # print store_msg  # To see store_msg value
        return store_msg

    def reader(self):
        """Read serial port."""
        counter = 1
        try:
            while self.serial.isOpen():
                counter += 1
                self.serial.write(str(chr(counter)))
                sleep(.1)
                if counter == 225:
                    counter = counter  # Reset counter
                self.dataread = self.serial.readline()
                logging.info(self.dataread)
                print self.dataread
        except serial.SerialException, e:
            self.alive = False
            print ("Error: ") + str(e)

    def menu(self):
        """Print menu for command selection."""
        print "--------------------------------------"
        print "Reader/Writer Tool for RS232 Device"
        print "--------------------------------------"
        print "Option :: "
        print "1. Write Command"
        print "2. Read Only"
        print "3. Configure Port"
        print "4. Process Msg Fields"
        print "0. Exit"
        print "\n"


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
        sp = SerialPort(port, baudrate, bytesize, parity, stopbits, timeout)
    except serial.SerialException, e:
        sys.stderr.write(HRED + "Port cannot be open %r: %s\n" % (port, e))
        sys.exit(1)

    sys.stderr.write(GRN + 'Reading port on %s with baudrate of %d\n' % (
        sp.serial.port,
        sp.serial.baudrate
    ) + WHT)

#    sp.start()
    sp.menu()
    while session == 1:
        cmdkey = raw_input(BLU + "Number Only. Key In Command: " + WHT)
        if cmdkey == "0":
            session = 0
            sp.stop()
        elif cmdkey == "1":
            print "Write command and send via serial port :  "
            return_msg = sp.writer()  # Nil count
            # sys.exit()
        elif cmdkey == "2":
            print "Read from serial port : "
            sp.reader()
        elif cmdkey == "3":
            print "Configuring serial port and baudrate : "
            sp.portconfig()
        elif cmdkey == "4":
            print "Processing message fields"
            endindex = procfieldvar()
            startindex = procprevfield()
            print return_msg[startindex:endindex]
        else:
            sp.menu()

#    try:
#        sp.join()
#    except KeyboardInterrupt:
#        pass
#    sys.stderr.write("\n >>> Exiting... ")
#    sp.join()


if __name__ == '__main__':
    main(sys.argv[1:])  # Take all arguments after 1st
