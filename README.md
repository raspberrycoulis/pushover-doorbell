# Pushover Doorbell

This is a very simple repository containing a couple of Python 3 scripts (coded on a Raspberry Pi) and a C++ script (coded for an ESP8266 board) that triggers a Pushover notification when a simple button, connected to the GPIO, is pushed.

On the Raspberry Pi, you can also use a connected NeoPixel for a visual indication that the doorbell has been pushed.

## Initial install

[Pushover](https://pushover.net) is a push notification platform, which costs $4.99 as a one-off payment for a lifetime license. It allows you to trigger push notifications very easily, which also work across multiple platforms. This code assumes you have a Pushover account already.

You'll need to create an app in your Pushover account (use a browser, not the app) and this will generate your app token. In the `doorbell.py` code you will need to insert your Pushover App and User API tokens in the relevant parts, before saving and exiting. You can then run the script to test.

By default, a simple push button is connected to GPIO 15 on the Raspberry Pi, but you can change this to any GPIO pin as long as you update the relevant part in the code.

### NeoPixels

To use NeoPixels (currently only on Raspberry Pi), you'll need to connect your NeoPixels to GPIO18 on the Pi (as this is [recommended by Adafruit](https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring)), then you'll need to [install the recommended modules](https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage):

```bash
sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
```
### NumPy in Python 3

To install NumPy as needed in the `fade-neopixel-doorbell.py` script, you'll likely run into issues with compatibility. To fix this, run:

```bash
sudo apt-get install libatlas-base-dev
sudo python3 -m pip install numpy
```
If you have no intention of using `fade-neopixel-doorbell.py` then you can ignore this bit.

### ESP8266

When using the ESP8266, the push button is connected between the D2 and the GND pins. If you wish to use a different pin, simply change the pin setting in the [esp8266-pushover-button.ino](https://github.com/raspberrycoulis/pushover-doorbell/blob/main/arduino/esp8266-pushover-button.ino) example. You will also need to provide your WiFi network credentials for this to work.

## Example wiring diagram
### Raspberry Pi

Below is an example of how a single NeoPixel and push-button can be wired to a Raspberry Pi's GPIO, which in this case is wired as follows:

* NeoPixel VCC - `5V`
* NeoPixel GND - `GND`
* NeoPixel DIN - `GPIO 18`
* Push-button (any pin works) - `GPIO 15`
* Push-button GND (any pin works) - `GND`

The push-button is very simple and you can use any pin for the ground / input. If unsure, stick with the diagram below:

![Fritzing Diagram](https://github.com/raspberrycoulis/pushover-doorbell/blob/main/content/fritzting.png)
