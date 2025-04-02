import numpy as np # type: ignore
import RPi.GPIO as GPIO # type: ignore
import csv
import datetime
import time
    

global sec
file = open('Lab10_Data.csv', 'w', newline = None)

csvwriter = csv.writer(file, delimiter = ',')

csvwriter.writerow(["Time", "Count"])
base = datetime.datetime.now()
def my_callback(channel):
    global count
    t=datetime.timedelta(base).seconds
    count+=1
    print(f"Time: {t}")
    print(f"Count: {count}")
    csvwriter.writerow([t,count])


global count
count=0
global channel
channel=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)
GPIO.setup(channel,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(channel,GPIO.FALLING,callback=my_callback)
while (datetime.datetime.now().second-base)<=20:
    time.sleep(10)

file.close()
