#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
    
    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()

    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

    # Print UID
	print uid[0],uid[1],uid[2],uid[3]
		
		#uid0 = uid[0]
		#uid1 = uid[1]
		#uid2 = uid[2]
		#uid3 = uid[3]
		#uid_Gesamt = uid0 + uid1 + uid2 + uid3
		#print UID_Gesamt
			
	if uid[3] == 121: #fetch the right RFID-Card

		
		# how to count the Pins
		GPIO.setmode(GPIO.BOARD)
		# get Pin 11  as output
		GPIO.setup(11, GPIO.OUT)
		 
		# ask if output is low
		if GPIO.input(11) == GPIO.LOW:
			# if output is low print this message
			print "Light will be switched on"
			time.sleep(1)
			# and set output to high (switch the light on)
			GPIO.output(11, GPIO.HIGH)
			
		# outherwise is output is high
		elif GPIO.input(11) == GPIO.HIGH:
			# printthis message
			print "Light will be switched off"
			time.sleep(1)
			#an set the output to low (switch the light off)
			GPIO.output(11, GPIO.LOW)
			GPIO.cleanup()
	else:
		#if the RFID Card isn't the one we are looking for
		print "Unknown/Wrong RFID Modul"
		
        
