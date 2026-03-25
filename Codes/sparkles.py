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

pixels.fill((0,0,0))



while True:
    p1 = random.randrange(0,45)
    p2 = random.randrange(46,97)
    c1 = random.randrange(10,255)
    c2 = random.randrange(10,255)
    c3 = random.randrange(10,255)
    #print(p)
    pixels[p1] =(c1,c2,c3)
    #pixels.show()
    pixels[p2] =(c3,c1,c2)
    pixels.show()
    sleep(0.01)
    #pixels.fill((0,0,0))

  



#pixels[45]=(0, 255, 0)
#pixels.show
#sleep(10)
#pixels.fill((0,0,0))
