import os
import time


DIRECTORY = 'C:/Users/DELL/Desktop/delete_testas'
SEVEN_DAYS = 60*60*24*7

def delete():
    for filename in os.scandir(DIRECTORY):
        if SEVEN_DAYS > (time.time() - os.path.getctime(filename)):
            print(DIRECTORY+"/"+filename.name)
            os.chmod(DIRECTORY+"/"+filename.name, 0o777)
            os.remove(DIRECTORY+"/"+filename.name)
        
if __name__ == "__main__":
    delete()