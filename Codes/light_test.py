import board
import neopixel
from time import sleep

pixel_pin = board.D18


# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.


num_pixels = 97

ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.01, auto_write=False, pixel_order=ORDER
)

#test
#pixels.fill((0,0,0))
#pixels.show()
#sleep(1)

#Top shoulders to arms
shouldersOne = (36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59)
for i in shouldersOne:
    pixels[i]=((0,0,255))
    pixels.show()
    sleep(0.2)

#Second shoulders to arms
shouldersTwo = (28, 29, 30, 31, 32, 33, 34, 35, 60, 61, 62, 63, 64, 65, 66, 67)
for i in shouldersTwo:
    pixels[i]=((255,255,0))
    pixels.show()
    sleep(0.2)  



#pixels[45]=(0, 255, 0)
#pixels.show
#sleep(10)
#pixels.fill((0,0,0))
