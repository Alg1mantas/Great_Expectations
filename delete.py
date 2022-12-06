import os
import time

DIRECTORY = 'C:/Users/DELL/Desktop/delete_testas'
SEVEN_DAYS = 60*60*24*7

for filename in os.scandir(DIRECTORY):
    if (time.time() - os.path.getctime(filename)) > SEVEN_DAYS:
        # print(filename.name)
        os.remove(DIRECTORY+"/"+filename.name)
        