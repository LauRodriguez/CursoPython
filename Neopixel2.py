# Circuit Playground NeoPixel
import time
import board
import neopixel
import digitalio

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

# choose which demos to play
# 1 means play, 0 means don't!
color_chase_demo = 1

led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()
button = digitalio.DigitalInOut(board.BUTTON_A)
button.switch_to_input(pull=digitalio.Pull.DOWN)

def color_chase(color, wait):
    for i in range(10):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.5)

BLUE = (0, 0, 255)
OFF = (0, 0, 0)

on=False
while True:
    if button.value and not on: # button is pushed
        led.value = True
        color_chase(BLUE, 0.2)
        on=True
    if button.value and on:
        color_chase(OFF, 0.2)
        led.value = False
        on=False

