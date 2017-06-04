Python Serial Interface

-- Use the below command in terminal to check ports

	dmesg | grep tty

-- CONFIGURE the serial port and baudrate by using portconfig.py
-- All other settings can be added on pyintf.py

-- Log is saved in the directory of the script

-- To configure serial

	serial.Serial(
		....
		)

