import csv
import time
import numpy as np

file = open('test.csv','w',newline=None)

csvwriter = csv.writer(file, delimiter=',')

csvwriter.writerow(['Timme','Data'])

for i in range(10):
    now=time.time()
    value=np.random()
    csvwriter.writerow([now,value])
    time.sleep(1)

file.close()