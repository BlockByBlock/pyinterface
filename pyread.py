#!/usr/bin/python

"""
pyread.

~~~~~~~~~~
This module reads from serial using python.
It logs the serial data in the same directory.
"""
from openport import open_port
import logging
from time import sleep

ser = open_port(None)

logging.basicConfig(
    filename='serial.log',
    filemode='w',
    format='',
    level=logging.DEBUG
)
# Global variables


# Main function
def data_output():
    """Log and print serial data."""
    if ser.isOpen():
        try:
            ser.reset_input_buffer()
            ser.reset_output_buffer()
            while True:
                counter = 32  # Below 32 for ASCII not needed
                counter += 1
                ser.write(str(chr(counter)))  # convert to string
                sleep(.1)
                if counter == 255:
                    counter = counter  # Reset counter
                readData = ser.readline()
                logging.info(readData)
                print readData
        except Exception, e1:
            print ("Error: ") + str(e1)
    else:
        print ("Cannot open serial port ")


# Run main function
if __name__ == '__main__':
    data_output()
