

import time
import os
import usb_hid
import digitalio
import board
import digitalio
import random

from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

led.value = False
time.sleep(3)

if not 'a.txt' in os.listdir():
    time.sleep(1.5)
    led.value=True
    keyboard = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(keyboard)

    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(1)
    layout.write("notepad")
    time.sleep(1)
    keyboard.send(Keycode.ENTER)
    time.sleep(1)
    keyboard.send(Keycode.ALT, Keycode.SPACE)
    time.sleep(1)
    layout.write("x")
    time.sleep(1)
    layout.write("subscribe to my channel now ==> https://youtube.com/c/hackwithvyshu")
    time.sleep(1)



while True:
    led.value = True
    time.sleep(0.1)
    led.value = False
    time.sleep(0.1)
