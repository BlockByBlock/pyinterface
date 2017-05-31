Python Serial Read

-- Use the below command in terminal to check ports

	dmesg | grep tty

-- CONFIGURE the serial port by using portconfig.py

-- Logging is implemented in directory of the script

-- To configure serial

	serial.Serial(
		....
		)

-- To read ASCII value below 32

	change counter value of counter_write function
