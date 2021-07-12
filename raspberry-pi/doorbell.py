#!/usr/bin/env python3

from time import sleep
from gpiozero import Button
import http.client, urllib

button = Button(15)    # Define the GPIO pin here (BCM numbering)

def pushover():
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
      urllib.parse.urlencode({
        "token": "ADD_APP_TOKEN_HERE",              # Insert app token here
        "user": "ADD_USER_TOKEN_HERE",              # Insert user token here
        "html": "1",                                # 1 for HTML, 0 to disable
        "title": "Doorbell",                        # Title of the message
        "message": "Somebody is at the front door", # Content of the message
        "sound": "pushover",                        # Define the sound played - default is a doorbell sound
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

while True:
    if button.is_pressed:
        pushover()
        sleep(10)    # To prevent spamming you with notifications
    else:
        continue
