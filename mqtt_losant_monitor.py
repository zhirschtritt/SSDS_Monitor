#!/usr/bin/env python

import time
from losantmqtt import Device
import RPi.GPIO as GPIO
from datetime import datetime
import pytz

from secrets import device

######### SET GPIO PINS  ###########
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
###################################

isVFDactive = GPIO.input(7)

print "Monitor Running..."


# def formatTextString():
#     easternTime = datetime.now(pytz.timezone('US/Eastern'))
#     fmt = '%Y%m%d %H:%M'
#     dateAndtime = easternTime.strftime(fmt)
#     date, time = dateAndtime.split(" ")
#     print ("date: " + date)
#     print("time: " + time)
#     siteRTN = "1-0012345"
#     deviceNumber = "1"
#     eventDescription = "shutdown"
#     emailString = str('"' + siteRTN + '","' + deviceNumber + '","' + eventDescription + '","' + date + '","' + time + '"')
#     print emailString
#     return emailString


def sendStateChange(channel):
    isVFDactive = GPIO.input(7)
    if device.is_connected():
        device.send_state({
            "isVFDactive": isVFDactive,
            #"emailString": formatTextString()
        })
    print ("Sending VFD state change to Losant")

try:
    GPIO.add_event_detect(7, GPIO.BOTH, callback=sendStateChange, bouncetime=300)

    device.connect()

except KeyboardInterrupt:
    print "Keyboard Interrupt"

finally:
    GPIO.cleanup()


# def on_command(device, command):
#     print("Command received.")
#     print(command["name"])
#     print(command["payload"])

# # Listen for commands.
# device.add_event_observer("command", on_command)

# Connect to Losant.


# Send temperature once every second.
# while True:
#     device.loop()
#     if device.is_connected():
#         temp = call_out_to_your_sensor_here()
#         device.send_state({"temperature": temp})
#     time.sleep(1)
