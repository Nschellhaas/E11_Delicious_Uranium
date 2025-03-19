import numpy as np # type: ignore
import RPi.GPIO as GPIO # type: ignore
import datetime
import time

def my_callback(channel):
    global count
    if GPIO.event_detected(channel):
        print(datetime.datetime.now())
        count+=1
    else:
        print(None)


global count
count=0
channel=11
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(channel,GPIO.FALLING,callback=my_callback)
while True:
    print(count)
    time.sleep(1)
    break