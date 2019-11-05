#Chris Salehi
#Alfonso Ramirez
#Group 8

#name code
#nano BLINK3LED.py
#begin writing code and initalize GPIO
import RPi.GPIO as GPIO
import time
#use BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Setup GPIO pins for LEDs
GPIO.setup(13, GPIO.OUT)
#Red LED is GPIO13
GPIO.setup(19, GPIO.OUT)
#Green LED is GPIO19
GPIO.setup(26, GPIO.OUT)
#Yellow LED is GPIO26
#Get Inputs
orderBlink = raw_input("Order of Blink? RGY or RYG?")
#Run inputs based on order selected, number of blinks, and speed of blinks
if orderBlink == "RGY":
    numTimes = raw_input("How many blinks for each LED?")
    blinkSpeed = raw_input("Blink speed in seconds for each LED?")
    num = int(numTimes)
    speed = float(blinkSpeed)
	for i in (range(0, num)):
		print "Red LED on"
		GPIO.output(13, GPIO.HIGH)
		time.sleep(2*speed)
		print "Red LED off"
		GPIO.output(13, GPIO.LOW)
		time.sleep(speed)
		print "Red blinked " + str(i+1) + " times"
	for j in (range (0, num)):
		print "Green LED on"
		GPIO.output(19, GPIO.HIGH)
		time.sleep(2*speed)
		print "Green LED off"
		GPIO.output(19, GPIO.LOW)
		time.sleep(speed)
		print "Green blinked " + str(j+1) + " times"
	for k in (range (0, num)):
		print "Yellow LED on"
		GPIO.output(26, GPIO.HIGH)
		time.sleep(2*speed)
		print "Yellow LED off"
		GPIO.output(26, GPIO.LOW)
		time.sleep(speed)
		print "Yellow blinked " + str(k+1) + " times"
    print "Completed " + str(i+1) " Red Blinks"
    print "Completed " + str(j+1) " Green Blinks"
    print "Completed " + str(k+1) " Yellow Blinks"
elif orderBlink == "RYG":
    numTimes = raw_input("How many blinks for each LED?")
    blinkSpeed = raw_input("Blink speed in seconds for each LED?")
    num = int(numTimes)
    speed = float(blinkSpeed)
	for i in (range(0, num)):
		print "Red LED on"
		GPIO.output(13, GPIO.HIGH)
		time.sleep(2*speed)
		print "Red LED off"
		GPIO.output(13, GPIO.LOW)
		time.sleep(speed)
		print "Red blinked " + str(i+1) + " times"
	for k in (range (0, num)):
		print "Yellow LED on"
		GPIO.output(26, GPIO.HIGH)
		time.sleep(2*speed)
		print "Yellow LED off"
		GPIO.output(26, GPIO.LOW)
		time.sleep(speed)
		print "Yellow blinked " + str(k+1) + " times"
	for j in (range (0, num)):
		print "Green LED on"
		GPIO.output(19, GPIO.HIGH)
		time.sleep(2*speed)
		print "Green LED off"
		GPIO.output(19, GPIO.LOW)
		time.sleep(speed)
		print "Green blinked " + str(j+1) + " times"
    print "Completed " + str(i+1) " Red Blinks"
    print "Completed " + str(j+1) " Green Blinks"
    print "Completed " + str(k+1) " Yellow Blinks"
 else:
    print "Please run code again and choose RGY or RYG"
#End code and display total number of blinks for each LED
GPIO.cleanup()

#run code
#sudo python BLINK3LED.py