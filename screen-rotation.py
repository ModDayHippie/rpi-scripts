import os
import time

#this script is made for use with rasbian cli

mode = input('do you want normal display or dev display( dev/norm):')


if mode == 'dev':
     print('change "display_hdmi_rotate=x" to "display_hdmi_rotate=3"')
     print('on botton line, save after with ctrl+x and then y and enter')
     time.sleep(3)
     os.system("sudo nano /boot/config.txt")
