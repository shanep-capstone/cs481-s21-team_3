import RPi.GPIO as GPIO
import time
#########################################
# Motion Sensor
#
# Basic PIR motion sensor setup using 
# python 3 and the raspberry pi 3. Simply 
# detects motion and counts the number of
# times motion is detected. 
#
# Usage:
#   $ python3 motion_sensor.py
#########################################
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# PIR motion sensor is connected to pin number 23 on the raspberry pi.
pir_sensor = 23 

GPIO.setup(pir_sensor, GPIO.IN, GPIO.PUD_DOWN)

# Detect motion, 0 means no motion detected, 1 means motion has been detected.
motion_detection = 0 

# Counter for the number of times motion has been detected.
num_motions = 1

try:
	while True:
		time.sleep(0.1)
        # Assigning GPIO value to our motion dection variable.
		motion_detection = GPIO.input(pir_sensor)
		if(motion_detection == 1):
			print("Motion detected!")
			print("Motion dection number: " + str(num_motions))
			num_motions += 1 # Increment number of motion detections.
			time.sleep(5) # Allow time for motion sensor to reset.
except:
    # Clean breakdown GPIO object and exit program
	GPIO.cleanup()
