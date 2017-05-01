import RPi.GPIO as GPIO
import time

######### SET GPIO PINS  ###########
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
###################################

isVFDactive = GPIO.input(7)


def send_message(channel):
    isVFDactive = GPIO.input(7)
    if isVFDactive == False:
        print 'shutdown detected: ' + str(isVFDactive)
    else:
        print "restart detected: " + str(isVFDactive)

GPIO.add_event_detect(7, GPIO.BOTH, callback=send_message, bouncetime=300)

while True:
    print GPIO.input(7)
    time.sleep(1)
