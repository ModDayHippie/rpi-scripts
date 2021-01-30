import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


print('this is a simple script that runs a led though the gpio')
time.sleep(3)
input('press Enter to run script')
print('-------------------------------------------')

GPIO.setup(18,GPIO.OUT0


GPIO.output(18,GPIO.HIGH)
time.sleep(5)

print('the led is now off')

GPIO.output(18,GPIO.LOW)

print('----------------------------------------------')
input('press ENTER to exit')
