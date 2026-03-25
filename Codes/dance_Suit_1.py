import board
import neopixel
from time import sleep

pixel_pin = board.D18


# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.


num_pixels = 97

ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.4, auto_write=False, pixel_order=ORDER
)

#test
pixels.fill((0,0,0))
pixels.show()
sleep(1)

#Top shoulders to arms
shouldersOne = (36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59)
for i in shouldersOne:
    pixels[i]=((255,0,0))
    pixels.show()
    sleep(0.1)

#Second shoulders to arms
shouldersTwo = (28, 29, 30, 31, 32, 33, 34, 35, 60, 61, 62, 63, 64, 65, 66, 67)
for i in shouldersTwo:
    pixels[i]=((255,255,0))
    pixels.show()
    sleep(0.1)  

#Middle chest down front
chestFront = (20, 21, 22, 23, 24, 25, 26, 27, 68, 69, 70, 71, 72, 73, 74, 75, 76)
for i in chestFront:
    pixels[i]=((255,255,255))
    pixels.show()
    sleep(0.1)

#Left Leg Top
leftLegTop = (77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87)
for i in leftLegTop:
    pixels[i]=((0,0,255))
    pixels.show()
    sleep(0.1)

#Left Leg Mid
leftLegMid = (88, 89, 90, 91, 92, 93, 94)
for i in leftLegMid:
    pixels[i]=((0,255,0))
    pixels.show()
    sleep(0.1)

#Left Leg Bottom
leftLegBottom = (95, 96)
for i in leftLegBottom:
    pixels[i]=((200,0,200))
    pixels.show()
    sleep(0.1)  

#Right Leg Top
rightLegTop = (19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9)
for i in rightLegTop:
    pixels[i]=((255,255,255))
    pixels.show()
    sleep(0.1)       

#Right Leg Mid
rightLegMid = (8, 7, 6, 5, 4, 3, 2)
for i in rightLegMid:
    pixels[i]=((0,255,255))
    pixels.show()
    sleep(0.1)

#Right Leg Bottom
rightLegBottom = (1, 0)
for i in rightLegBottom:
    pixels[i]=((124,140,255))
    pixels.show()
    sleep(0.1)      


#pixels[45]=(0, 255, 0)
#pixels.show
#sleep(10)
#pixels.fill((0,0,0))
