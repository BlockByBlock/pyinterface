#!/usr/bin/python

"""
portconfig.

~~~~~~~~~~
This module configure and save the port and baudrate.
"""

config_file = open("portconfig.txt", "w")

cport = raw_input("Set port (e.g. /dev/ttyUSB0) :: ")
config_file.write(cport)
print ("Port is configured as " + cport)
config_file.write("\n")
cbaudrate = raw_input("Set baudrate (e.g. 9600, 57600, 115200) :: ")
config_file.write(cbaudrate)
print ("Baudrate is configured as " + cbaudrate)

# config_file.close()

print "\nPort configured successful!"
