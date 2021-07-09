# Pushover Doorbell

This is a very simple Python 3 script (coded on a Raspberry Pi) that triggers a Pushover notification when a simple button, connected to the GPIO, is pushed.

## Initial install

[Pushover](https://pushover.net) is a push notification platform, which costs $4.99 as a one-off payment for a lifetime license. It allows you to trigger push notifications very easily, which also work across multiple platforms. This code assumes you have a Pushover account already.

You'll need to create an app in your Pushover account (use a browser, not the app) and this will generate your app token. In the `doorbell.py` code you will need to insert your Pushover App and User API tokens in the relevant parts, before saving and exiting. You can then run the script to test.

By default, a simple push button is connected to GPIO 15 on the Raspberry Pi, but you can change this to any GPIO pin as long as you update the relevant part in the code.
