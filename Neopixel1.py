# Circuit Playground NeoPixel
import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.2, auto_write=False)

# choose which demos to play
# 1 means play, 0 means don't!
color_chase_demo = 1


def color_chase(color, wait):
    for i in range(10):
        pixels[i] = color
        time.sleep(wait)
        pixels.show()
    time.sleep(0.1)


BLUE = (0, 0, 255)
OFF = (0, 0, 0)

while True:
    if color_chase_demo:
        
        color_chase(BLUE, 0.6)
        color_chase(OFF, 0.8)
