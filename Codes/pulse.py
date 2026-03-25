import board
import neopixel
from time import sleep
import random

pixel_pin = board.D18


# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.

num_pixels = 97

ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.01, auto_write=False, pixel_order=ORDER
)

bright = 0.01

pixels.fill((0,0,0))
pixels.show()



while True:
    if bright > 0.3:
        pixels.fill((0,0,0))
        pixels.show()
        sleep(0.8) 
        bright = 0
    else:
        pixels.brightness=bright
        pixels.fill((255,255,255))
        pixels.show()
        bright += 0.01
        sleep(0)
        print(bright)
        
        

