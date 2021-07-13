#!/usr/bin/env python3

import board
import neopixel
import datetime
from time import sleep
from gpiozero import Button
import http.client, urllib

# Setup stuff first
button = Button(15)    # Define the GPIO pin here (BCM numbering)
pixel_pin = board.D18  # BCM pin (18 is default and recommended)
num_pixels = 1         # Set the number of NeoPixels used here
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.5)
OFF = (0, 0, 0)

def pushover():
    now = datetime.datetime.now()
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
      urllib.parse.urlencode({
        "token": "ADD_HERE",              # Insert app token here
        "user": "ADD_HERE",              # Insert user token here
        "html": "1",                                # 1 for HTML, 0 to disable
        "title": "Doorbell",                        # Title of the message
        "message": "Doorbell pushed at " + now.strftime("%H:%M:%S on %d/%m/%Y"), # Content of the message
        "sound": "pushover",                        # Define the sound played - default is a doorbell sound
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

def flash_red():
    for i in range(0, 4 * 256, 8):
        for j in range(num_pixels):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            pixels[j] = (val, 0, 0)
        pixels.write()

def flash_green():
    for i in range(0, 4 * 256, 8):
        for j in range(num_pixels):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            pixels[j] = (0, val, 0)
        pixels.write()

while True:
    now = datetime.datetime.now()
    if button.is_pressed:
        print("Somebody is at the door at "+ now.strftime("%H:%M:%S on %d/%m/%Y"))
        pushover()
        flash_red()
        flash_green()
        flash_red()
        flash_green()
        flash_red()
        flash_green()
        flash_red()
        flash_green()
        flash_red()
        flash_green()
        flash_red()
        flash_green()
        flash_red()
        flash_green()
        flash_red()
        flash_green()
        flash_red()
        flash_green()
        flash_red()
        flash_green()
        flash_red()
        flash_green()
        flash_red()
        flash_green()
    else:
        pixels[0] = OFF
        continue
