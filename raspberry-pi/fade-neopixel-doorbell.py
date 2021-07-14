#!/usr/bin/env python3

import board
import neopixel
import datetime
import os, sys
from gpiozero import Button
from time import sleep
import numpy as np
import http.client, urllib


# Check that the code is being run as root, and exit if not
if not os.geteuid()==0:
    sys.exit("This script must be run with 'sudo'!")

# Some set up for the button and NeoPixels
button = Button(15)
pixel_pin = board.D18
num_pixels = 1
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2)

# Define some colours to save typing RGB numbers eveywhere
BLUE = (0,0,255)
GREEN = (0,255,0)
LIME = (191,255,0)
WHITE = (255,255,255)

# The colours to be cycled through. If adding more, increase 
# the `if j ==3:` in the cycle function to the number of colours minus 1
my_colours = [GREEN,LIME,GREEN,LIME]

# The function that triggers Pushover
def pushover():
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
      urllib.parse.urlencode({
        "token": "ADD_HERE",                        # Insert app token here
        "user": "ADD_HERE",                         # Insert user token here
        "html": "1",                                # 1 for HTML, 0 to disable
        "title": "Doorbell",                        # Title of the message
        "message": "Somebody is at the door!",      # Content of the message
        "sound": "pushover",                        # Define the sound played - default is a doorbell sound
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

# The function that determines the fade between colours
def fade(colour1, colour2, percent):
    colour1 = np.array(colour1)
    colour2 = np.array(colour2)
    vector = colour2-colour1
    newcolour = (int((colour1 + vector * percent)[0]), int((colour1 + vector * percent)[1]), int((colour1 + vector * percent)[2]))
    return newcolour

# The function that cycles through the colours
def cycle(wait):
    for j in range(len(my_colours)):
        for i in range(10):
            colour1 = my_colours[j]
            if j == 3:
                colour2 = WHITE
            else:
                colour2 = my_colours[(j+1)]
            percent = i*0.1
            pixels.fill((fade(colour1,colour2,percent)))
            pixels.show()
            sleep(wait)

# Sets the NeoPixel(s) to blue when started
pixels.fill(BLUE)
pixels.show()

# The main code
while True:
    sleep(1)
    button.wait_for_press()
    now = datetime.datetime.now()
    print("Somebody is at the door at "+ now.strftime("%H:%M:%S on %d/%m/%Y"))
    pushover()
    for _ in range(5):     # Loop the cycle function 5 times (approx 10 secs)
        cycle(0.05)
