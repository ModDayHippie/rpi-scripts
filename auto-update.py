import os
import time

print('this script will automatily update and install all installed repos')
print('-----------------------------------------------')
time.sleep(2)
print('updating repos ')
print('-----------------------------------------------')
os.system("sudo apt-get update")
print('-----------------------------------------------')
time.sleep(1)
print('installing updates if any')
print('-----------------------------------------------')
os.system("sudo apt-get update")
time.sleep(1)
print('-----------------------------------------------')
print('system repos have been updated')
print('-----------------------------------------------')
