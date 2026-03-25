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
pixels.show()
sleep(10)

while True:
    p1 = random.randrange(0,45) #left pixels
    p2 = random.randrange(46,97) #right pixels
    print (p1, p2)    
    red1 = random.randrange(5,255)
    red2 = random.randrange(5,255)
    #print(p)
    pixels[p1] =(0,red1,0)
    
    pixels[p2] =(0,red2,0)
    pixels.show()
    sleep(0.001)
    

  



#pixels[45]=(0, 255, 0)
#pixels.show
#sleep(10)
#pixels.fill((0,0,0))
