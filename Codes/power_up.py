import board
import neopixel
from time import sleep

pixel_pin = board.D18


# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.


num_pixels = 97

ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.5, auto_write=False, pixel_order=ORDER
)

#test
pixels.fill((0,0,0))
pixels.show()
sleep(1)

left = 48
right  = 47

#Top shoulders to bottom

while True:
    if right > -1:
        pixels[left]=((255,255,255))
        pixels[right]=((255,255,255))
        pixels.show()
        sleep(0.03)
        left += 1
        right -= 1
        print (left, right)
        pixels.fill((0,0,0))
    else:
        #pixels.fill((255,255,255)) # use to flash bright
        pixels.fill((0,0,0))
        pixels.show()
        #sleep(5)
        left = 48
        right  = 47
   

