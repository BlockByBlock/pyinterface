#!/usr/bin/python

"""
pymisca.

~~~~~~~~~~
This module reads misca response using python.
-- ybingcheng@gmail.com
"""

from openport import open_port
from time import sleep
import sys

GRN = '\033[32m'
WHT = '\033[0m'

fchar = 0  # First field

msgLength = 498

# All in characters, otherwise commented
MC_misca = (fchar + 5)  # Response to SNDA
MC_706 = (MC_misca + 3)  # Bytes between STX and CR
MC_97 = (MC_706 + 2)  # Bytes between STX and ETX
# 02 HEX
MC_STX = (MC_97 + 4)  # Start of transmission character
MC_F5 = (MC_STX + 6)  # Ventilator time
MC_F6 = (MC_F5 + 18)  # Ventilator ID
MC_F7 = (MC_F6 + 6)  # Not used
MC_F8 = (MC_F7 + 12)  # Date
MC_F9 = (MC_F8 + 6)  # Mode
MC_F10 = (MC_F9 + 6)  # Respiratory rate
MC_F11 = (MC_F10 + 6)  # Tidal volume
MC_F12 = (MC_F11 + 6)  # Peak flow
MC_F13 = (MC_F12 + 6)  # O2 setting
MC_F14 = (MC_F13 + 6)  # Pressure sensitivity setting
MC_F15 = (MC_F14 + 6)  # PEEP setting
MC_F16 = (MC_F15 + 6)  # Plateau time
MC_F17_20 = (MC_F16 + 6)  # Not used
MC_F21 = (MC_F17_20 + 6)  # Apnea interval
MC_F22 = (MC_F21 + 6)  # Apnea tidal volume setting
MC_F23 = (MC_F22 + 6)  # Apnea resp rate setting
MC_F24 = (MC_F23 + 6)  # Apnea peak flow setting
MC_F25 = (MC_F24 + 6)  # Apnea O2 setting
MC_F26 = (MC_F25 + 6)  # Pressure support setting
MC_F27 = (MC_F26 + 6)  # Flow pattern setting
MC_F28_29 = (MC_F27 + 6)  # Not used
MC_F30 = (MC_F28_29 + 6)  # 100% O2 state
MC_F31_33 = (MC_F30 + 6)  # Not used
MC_F34 = (MC_F31_33 + 6)  # Total resp rate
MC_F35 = (MC_F34 + 6)  # Exhaled tidal volume
MC_F36 = (MC_F35 + 6)  # Exhaled minute volume
MC_F37 = (MC_F36 + 6)  # Spontaneous minute volume
MC_F38 = (MC_F37 + 6)  # Max circuit pressure
MC_F39 = (MC_F38 + 6)  # Mean airway pressure
MC_F40 = (MC_F39 + 6)  # End inspiratory pressure
MC_F41 = (MC_F40 + 6)  # Exp component of monitored value
MC_F42 = (MC_F41 + 6)  # High circuit pressure limit
MC_F43_44 = (MC_F42 + 6)  # Not used
MC_F45 = (MC_F43_44 + 6)  # Low exhaled tidal volume
MC_F46 = (MC_F45 + 6)  # Low exhaled minute volume
MC_F47 = (MC_F46 + 6)  # High resp rate limit
MC_F48 = (MC_F47 + 6)  # High circuit pressure alarm status
MC_F49_50 = (MC_F48 + 6)  # Not used
MC_F51 = (MC_F49_50 + 6)  # Low exhaled tidal volume alarm status
MC_F52 = (MC_F51 + 6)  # Low exhaled minute volume alarm status
MC_F53 = (MC_F52 + 6)  # High resp rate alarm status
MC_F54 = (MC_F53 + 6)  # No O2 supply alarm status
MC_F55 = (MC_F54 + 6)  # No air supply alarm status
MC_F56 = (MC_F55 + 6)  # Not used
MC_F57 = (MC_F56 + 6)  # Apnea alarm status
MC_F58_59 = (MC_F57 + 6)  # Not used
MC_F60 = (MC_F58_59 + 6)  # Ventilator time
MC_F61 = (MC_F60 + 6)  # Not used
MC_F62 = (MC_F61 + 6)  # Date
MC_F63 = (MC_F62 + 6)  # Static compliance
MC_F64 = (MC_F63 + 6)  # Static resistance
MC_F65 = (MC_F64 + 6)  # Dynamic compliance
MC_F66 = (MC_F65 + 6)  # Dynamic resistance
MC_F67 = (MC_F66 + 6)  # Negative inspiratory force
MC_F68 = (MC_F67 + 6)  # Vital capacity
MC_F69 = (MC_F68 + 6)  # Peak spontaneous flow
MC_F70 = (MC_F69 + 6)  # Ventilator-set base flow
MC_F71 = (MC_F70 + 6)  # Flow sensitivity setting
MC_F72_83 = (MC_F71 + 6)  # Not used
MC_F84 = (MC_F72_83 + 6)  # End inspiratory pressure
MC_F85 = (MC_F84 + 6)  # Inspiratory pressure
MC_F86 = (MC_F85 + 6)  # Inspiratory time
MC_F87 = (MC_F86 + 6)  # Apnea interval setting
MC_F88 = (MC_F87 + 6)  # Apnea inspiratory pressure setting
MC_F89 = (MC_F88 + 6)  # Apnea respiratory rate setting
MC_F90 = (MC_F89 + 6)  # Apnea inspiratory time setting
MC_F91 = (MC_F90 + 6)  # Apnea O2 setting
MC_F92 = (MC_F91 + 6)  # Apnea high circuit pressure limit
MC_F93 = (MC_F92 + 6)  # Alarm silence state
MC_F94 = (MC_F93 + 6)  # Apnea alarm status
MC_F95 = (MC_F94 + 6)  # Severe Occlusion
MC_F96 = (MC_F95 + 6)  # Inspiratory component of IE high
MC_F97 = (MC_F96 + 6)  # Inspiratory component of IE low
MC_F98 = (MC_F97 + 6)  # Inspiratory component of apnea IE
MC_F99 = (MC_F98 + 6)  # Expiratory compinent of apnea IE
MC_F100 = (MC_F99 + 6)  # Constant during rate setting change
MC_F101 = (MC_F100 + 6)  # Monitored value of IE
# 03 HEX
MC_ETX = (MC_F101 + 4)
MC_CR = (MC_ETX + 1)
# END OF ALL FIELDS IN misca

ser = open_port(None)

cmd = raw_input("Send Command? >> ")
print GRN + "You have send " + cmd + " to serial port" + WHT
if cmd is not None:
    try:
        ser.write(cmd)
        print
        sleep(1)  # Delay
        response = ser.readline()
        sleep(1)
        response_one = ser.readline()  # Backup readline
        # respone_bb = ser.read(msgLength)  # by byte
        sleep(1)
        response_two = ser.readline()  # Backup realine 2
        print response
        print response_one
        # print response_bb
        print response_two
        ser.close()
    except Exception, ew:
        print ("Error: ") + str(ew)
else:
    print "Exiting"
    sys.exit()
