#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import time
import lcddriver

lcd = lcddriver.lcd()
lcd.lcd_clear()

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print ("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()
    lcd.lcd_clear()
    lcd.lcd_backlight("off")
    

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

# Welcome message
print ("Welcome to the MFRC522 data read example")
print ("Press Ctrl-C to stop.")
lcd.lcd_display_string("Bitte Chip", 1)
lcd.lcd_display_string("auflegen", 2)

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:

    # Scan for cards    
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

    # If a card is found
    if status == MIFAREReader.MI_OK:
        print ("Card detected")
    
    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

    # Print UID
                        
        print (str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3]))
			
        if str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3]) == ("2315839121") or str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])  == ("1364147115"): #fetch the right RFID-Card

		
            # how to count the Pins
            GPIO.setmode(GPIO.BOARD)
            # get Pin 11  as output
            GPIO.setup(11, GPIO.OUT)
		 
            # ask if output is low
            if GPIO.input(11) == GPIO.LOW:
                # if output is low print this message
                print ("Light will be switched on")
                lcd.lcd_clear()
                lcd.lcd_display_string ("Licht wird ", 1)
                lcd.lcd_display_string ("angeschaltet", 2)
                time.sleep(1.5)
                lcd.lcd_clear()
                lcd.lcd_display_string("Bitte Chip", 1)
                lcd.lcd_display_string("auflegen", 2)
                # and set output to high (switch the light on)
                GPIO.output(11, GPIO.HIGH)
			
                # outherwise is output is high
            elif GPIO.input(11) == GPIO.HIGH:
                # printthis message
                print ("Light will be switched off")
                lcd.lcd_clear()
                lcd.lcd_display_string ("Licht wird", 1)
                lcd.lcd_display_string ("ausgeschaltet", 2)
                time.sleep(1.5)
                lcd.lcd_clear()
                lcd.lcd_display_string("Bitte Chip", 1)
                lcd.lcd_display_string("auflegen", 2)
                #and set the output to low (switch the light off)
                GPIO.output(11, GPIO.LOW)
                #GPIO.cleanup()
        else:
        #if the RFID Card isn't the one we are looking for
            print ("Unknown/Wrong RFID Modul")
            lcd.lcd_clear()
            lcd.lcd_display_string("Falscher Chip", 1)
            time.sleep(1.5)
            lcd.lcd_clear()
            lcd.lcd_display_string("Bitte Chip", 1)
            lcd.lcd_display_string("auflegen", 2)

