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
    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
)

#test
pixels.fill((0,0,0))
pixels.show()
sleep(1)

# bottom left = 96 bottom right = 0

left = 48
right  = 47

#Top shoulders to bottom
while True:
    while left != 97 and right != 0:
        pixels[left]=((255,255,255))
        pixels[right]=((255,255,255))
        pixels.show()
        sleep(0.1)
        left += 1
        right -= 1
        pixels.fill((0,0,0))
        print (left, right)
    left = 48
    right = 47
   

