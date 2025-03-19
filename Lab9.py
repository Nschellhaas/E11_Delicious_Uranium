import numpy as np # type: ignore
import RPi.GPIO as GPIO # type: ignore
import datetime
import time



def my_callback(channel):
    global count
    print(datetime.datetime.now())
    print(count)
    count+=1


global count
count=0
global channel
channel=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)
GPIO.setup(channel,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(channel,GPIO.FALLING,callback=my_callback)
while True:
    time.sleep(10)

