#!/usr/bin/python
# Example using a character LCD plate (credits: https://github.com/adafruit/Adafruit_Python_CharLCD/blob/master/examples/char_lcd_plate.py)
import time

import Adafruit_CharLCD as LCD
import signal   # interrupt/timer library
import RPi.GPIO as GPIO

# Initialize the LCD using the pins
#lcd = LCD.Adafruit_CharLCDPlate()

# create some custom characters
#lcd.create_char(1, [0, 27, 27, 0, 4, 4, 17, 14])  # lachend mannetje
#lcd.create_char(2, [0, 1, 3, 22, 28, 8, 0, 0])
#lcd.create_char(3, [0, 14, 21, 23, 17, 14, 0, 0])
#lcd.create_char(4, [31, 17, 10, 4, 10, 17, 31, 0])
#lcd.create_char(5, [8, 12, 10, 9, 10, 12, 8, 0])
#lcd.create_char(6, [2, 6, 10, 18, 10, 6, 2, 0])
#lcd.create_char(7, [31, 17, 21, 21, 21, 21, 17, 31])

# Show some basic colors.
#lcd.set_color(1.0, 0.0, 0.0)
#lcd.clear()
#lcd.message('RED \x01')
#time.sleep(0.1)

#lcd.set_color(0.0, 1.0, 0.0)
#lcd.clear()
#lcd.message('GREEN \x02')
#time.sleep(0.1)

#lcd.set_color(0.0, 0.0, 1.0)
#lcd.clear()
#lcd.message('BLUE \x03')
#time.sleep(0.1)

#lcd.set_color(1.0, 1.0, 0.0)
#lcd.clear()
#lcd.message('YELLOW \x04')
#time.sleep(0.1)

#lcd.set_color(0.0, 1.0, 1.0)
#lcd.clear()
#lcd.message('CYAN \x05')
#time.sleep(0.1)

#lcd.set_color(1.0, 0.0, 1.0)
#lcd.clear()
#lcd.message('MAGENTA \x06')
#time.sleep(0.1)

#lcd.set_color(1.0, 1.0, 1.0)
#lcd.clear()
#lcd.message('WHITE \x07')
#time.sleep(0.1)

totalgoals = 0

# we define goal as an indication from sensor 16 followed by one of at least 20 or 21
triggered16 = False

# Define interrupt callback function
def my_callback(channel):
    global triggered16  # Make sure Python knows we want to use the global, not the local variable
    global totalgoals
    print(channel)
    if channel == 16:
        triggered16 = True
    elif (channel == 20 or channel == 21) and triggered16:
        totalgoals = totalgoals + 1
        triggered16 = False

        f = open('/var/www/html/index.html', 'w')

        message = """<html>
        <head><title>score</title><meta http-equiv="refresh" content="2"/></head>
        <body><h1>"""
        message = message + """<font size="120" color="red">GOALS: """ + str(totalgoals)
        message = message + """</font>
        </h1></body>
        </html>"""

        f.write(message)
        f.close()

# Configure main button
GPIO.setmode(GPIO.BCM) #Use Broadcom SOC Channel number (pin 40 == GPIO21), no choice as Adafruit uses this mode...
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(16, GPIO.FALLING, callback=my_callback)
GPIO.add_event_detect(20, GPIO.FALLING, callback=my_callback)
GPIO.add_event_detect(21, GPIO.FALLING, callback=my_callback)

# Show button state.
#lcd.clear()
#lcd.message('Hallo Wouter\n(druk op knop)')

# Make list of button value, text, and backlight color.
#buttons = ((LCD.SELECT, 'Select', (1, 1, 1)),
#           (LCD.LEFT, 'Left', (1, 0, 0)),
#           (LCD.UP, 'Up', (0, 0, 1)),
#           (LCD.DOWN, 'Down', (0, 1, 0)),
#           (LCD.RIGHT, 'Right', (1, 0, 1)))

print('Press Ctrl-C to quit.')


# Loop through each button and check if it is pressed (for use in specific code later)
try:
    while(True):
#        for button in buttons:
#            if lcd.is_pressed(button[0]):
            # Button is pressed, change the message and backlight.
#                lcd.clear()
#                lcd.message(button[1])
#               lcd.set_color(button[2][0], button[2][1], button[2][2])
        print("in loop")
        time.sleep(1000)


# This open() may hang indefinitely

#    while True:
#        print"."
#        time.sleep(5)
#
#    signal.alarm(0)          # Disable the alarm

finally:
    print("Resetting all GPIO to input to prevent dangers when changing hardware.")
    GPIO.cleanup()
