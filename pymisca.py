#!/usr/bin/python

"""
pymisca.

~~~~~~~~~~
This module reads misca response using python.
"""

from openport import open_port
from time import sleep

# All in characters, otherwise commented
MC_misca = 5  # Response to SNDA
MC_706 = 2  # Bytes between STX and CR
MC_97 = 2  # Bytes between STX and ETX
# 02 HEX
MC_STX = 2  # Start of transmission character
MC_F5 = 6  # Ventilator time
MC_F6 = 18  # Ventilator ID
MC_F7 = 6  # Not used
MC_F8 = 12  # Date
MC_F9 = 6  # Mode
MC_F10 = 6  # Respiratory rate
MC_F11 = 6  # Tidal volume
MC_F12 = 6  # Peak flow
MC_F13 = 6  # O2 setting
MC_F14 = 6  # Pressure sensitivity setting
MC_F15 = 6  # PEEP setting
MC_F16 = 6  # Plateau time
MC_F17_20 = 6  # Not used
MC_F21 = 6  # Apnea interval
MC_F22 = 6  # Apnea tidal volume setting
MC_F23 = 6  # Apnea resp rate setting
MC_F24 = 6  # Apnea peak flow setting
MC_F25 = 6  # Apnea O2 setting
MC_F26 = 6  # Pressure support setting
MC_F27 = 6  # Flow pattern setting
MC_F28_29 = 6  # Not used
MC_F30 = 6  # 100% O2 state
MC_F31_33 = 6  # Not used
MC_F34 = 6  # Total resp rate
MC_F35 = 6  # Exhaled tidal volume
MC_F36 = 6  # Exhaled minute volume
MC_F37 = 6  # Spontaneous minute volume
MC_F38 = 6  # Max circuit pressure
MC_F39 = 6  # Mean airway pressure
MC_F40 = 6  # End inspiratory pressure
MC_F41 = 6  # Exp component of monitored value
MC_F42 = 6  # High circuit pressure limit
MC_F43_44 = 6  # Not used
MC_F45 = 6  # Low exhaled tidal volume
MC_F46 = 6  # Low exhaled minute volume
MC_F47 = 6  # High resp rate limit
MC_F48 = 6  # High circuit pressure alarm status
MC_F49_50 = 6  # Not used
MC_F51 = 6  # Low exhaled tidal volume alarm status
MC_F52 = 6  # Low exhaled minute volume alarm status
MC_F53 = 6  # High resp rate alarm status
MC_F54 = 6  # No O2 supply alarm status
MC_F55 = 6  # No air supply alarm status
MC_F56 = 6  # Not used
MC_F57 = 6  # Apnea alarm status
MC_F58_59 = 6  # Not used
MC_F60 = 6  # Ventilator time
MC_F61 = 6  # Not used
MC_F62 = 6  # Date
MC_F63 = 6  # Static compliance
MC_F64 = 6  # Static resistance
MC_F65 = 6  # Dynamic compliance
MC_F66 = 6  # Dynamic resistance
MC_F67 = 6  # Negative inspiratory force
MC_F68 = 6  # Vital capacity
MC_F69 = 6  # Peak spontaneous flow
MC_F70 = 6  # Ventilator-set base flow
MC_F71 = 6  # Flow sensitivity setting
MC_F72_83 = 6  # Not used
MC_F84 = 6  # End inspiratory pressure
MC_F85 = 6  # Inspiratory pressure
MC_F86 = 6  # Inspiratory time
MC_F87 = 6  # Apnea interval setting
MC_F88 = 6  # Apnea inspiratory pressure setting
MC_F89 = 6  # Apnea respiratory rate setting
MC_F90 = 6  # Apnea inspiratory time setting
MC_F91 = 6  # Apnea O2 setting
MC_F92 = 6  # Apnea high circuit pressure limit
MC_F93 = 6  # Alarm silence state
MC_F94 = 6  # Apnea alarm status
# END OF ALL FIELDS IN misca

ser = open_port(None)

cmd = raw_input("Send Command? >> ")
print "You have send " + cmd + " to serial port"
if cmd is not None:
    try:
        ser.write(cmd)
        sleep(1)  # Delay
        response = ser.readline()
        sleep(1)
        response_two = ser.readline()
        sleep(1)
        response_three = ser.readline()
        print response
        print response_two
        print response_three
        ser.close()
    except Exception, ew:
        print ("Error: ") + str(ew)
else:
    print "Exiting"
    sys.exit()
