#!/usr/bin/python
#
# control fan based on temperature limit
#
# EZFan2 connected to standard RPi case fan
#
#               +--------+
# +-----+       |        +----5V
# |     +--red--+        |
# | FAN |       | EZFan2 +----GPIO
# |     +--blk--+        | 
# +-----+       |        +----GND
#               +--------+
#
# to set up in cron, copy the script to /home/pi/bin (assumes 'pi' is
# user name).  Add this entry to crontab (adjust pin and temp as needed):
#     */1 * * * * /home/pi/bin/fantemp.py --p 14 -t 60
#

import getopt, sys

pin = 14
temp_limit = 60.0
verbose = False

try:
    opts, args = getopt.getopt(sys.argv[1:],
        "p:t:v", ["pin=", "temp=", "verbose"])
except getopt.GetoptError:
    print "Usage: fantemp.py [-t <temperature] [-p <GPIO pin #>]"
    sys.exit(2)

for opt, arg in opts:
    if opt in ("-p", "--pin"):
        pin = int(arg)
    elif opt in ("-t", "--temp"):
        temp_limit = float(arg)
    elif opt in ("-v", "--verbose"):
        verbose = True

import RPi.GPIO as GPIO

from vcgencmd import Vcgencmd
vcgm = Vcgencmd()
cputemp = vcgm.measure_temp()
if verbose:
    import datetime
    now = datetime.datetime.now()
    print("%s cpu temp: %2.1f, limit: %2.1f" % (str(now), cputemp, temp_limit))

#use GPIO pin numbering not physical
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(pin, GPIO.OUT)
fanstate = GPIO.input(pin)

if cputemp > temp_limit:
    if fanstate == 0:
        GPIO.output(pin, GPIO.HIGH)
        if verbose:
            print("turn on fan via pin: %d" % pin)
elif cputemp < (temp_limit - 5.0):
    if fanstate == 1:
        if verbose:
            print("turn off fan via pin: %d" % pin)
        GPIO.output(pin, GPIO.LOW)
else:
    if verbose:
        print("leave fan on for a bit more cooling")

