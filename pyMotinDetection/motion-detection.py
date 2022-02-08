import RPi.GPIO as GPIO
import time

Input_Pin = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Input_Pin, GPIO.IN)

for x in range(0, 500):
    if GPIO.input(Input_Pin):
	print('Detection')
    else:
	print('No detection')
        time.sleep(0.1)
	
GPIO.cleanup()
print('Done')
