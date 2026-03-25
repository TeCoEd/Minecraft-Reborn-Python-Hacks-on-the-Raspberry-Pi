import board
import neopixel
from time import sleep
from datetime import datetime

pixel_pin = board.D18

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.

num_pixels = 97

ORDER = neopixel.RGB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
)

#left = 48 top 96 bottom
#right  = 47 top 0 bottom

while True:
    # Get the current date and time
    current_time = datetime.now()

    # Extract hours, minutes, and seconds
    hours = current_time.hour
    minutes = current_time.minute
    seconds = current_time.second

    # Print the extracted components
    print("Hours:", hours)
    print("Minutes:", minutes)
    print("Seconds:", seconds)

    hr = hours
    mins = minutes
    sec = seconds

    # WORKS OUT HOURS
    #TimeLEDS = [0,  1,  2,  3,  4,  5, 6, 7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24] TIME
    TimeLEDS =  [47, 39, 31, 23, 15, 7, 0, 88, 80, 72, 64, 56, 48, 39, 31, 23, 15, 7,  96, 88, 80, 72, 64, 56, 48] #LED light to display in order of the hour position

    print ("Hours LED", TimeLEDS[hr-1]) #dAYLIGHT sAVING?'

    led_number = TimeLEDS[hr] #dAYLIGHT sAVING?'

    # Display hour LED - GREEN
    pixels[led_number]=(0, 0, 255)
    pixels.show()

    # WORKS OUT MINS.
    print ("mins = ", mins)

    minuteLightPosition = mins * 1.6 - 1

    if mins == 0: # checks for new hour 00:00
        pixels[48]=(255, 255, 255)
        #pixels.show()
        pixels[47]=(255, 255, 255)
        pixels.show()
    if mins == 30: # checks for half past 30 mins
        pixels[96]=(255, 255, 255)
        #pixels.show()
        pixels[0]=(255, 255, 255)
        pixels.show()    
    elif mins < 30:
        #minuteLightPosition = mins * 1.6 - 1
        minuteLightPosition = 48 - (mins * 1.6) 
        print (minuteLightPosition)
        pixels[int(minuteLightPosition)]=(255, 255, 255)
        pixels.show()
    elif mins > 30:
        minuteLightPosition = 47 - (mins * 1.6) 
        print (minuteLightPosition)
        pixels[int(minuteLightPosition)]=(255, 255, 255)
        pixels.show()
    else:
        pixels[0]=(0, 255, 255)
        pixels.show()



    # WORKS OUT SECs.
    secLightPosition = mins * 1.6 - 1

    if sec == 0: # checks for new 60 seconds
        pixels[47]=(255, 255, 0)
        #pixels.show()
        pixels[48]=(255, 255, 0)
        pixels.show()
        sleep(1) # waits one second
        pixels[48] =(0, 0, 0) # clears the second LEDS from suit
        pixels[47] =(0, 0, 0)
        pixels.show()
    if sec == 30: # checks for 30 seconds
        pixels[96]=(255, 255, 0)
        #pixels.show()
        pixels[0]=(255, 255, 0)
        pixels.show()
        sleep(1)
        pixels[96] =(0, 0, 0)
        pixels[0] =(0, 0, 0)
        pixels.show()
    elif sec < 30:
        #minuteLightPosition = mins * 1.6 - 1
        secLightPosition = 48 - (sec * 1.6) 
        print (secLightPosition)
        pixels[int(secLightPosition)]=(255, 255, 0)
        pixels.show()
        sleep(1)
        pixels[int(secLightPosition)] =(0, 0, 0)  
    elif sec > 30:
        secLightPosition = 47 - (sec * 1.6) 
        print (secLightPosition)
        pixels[int(secLightPosition)]=(255, 255, 0)
        pixels.show()
        sleep(1)
        pixels[int(secLightPosition)] = (0, 0, 0)  
    else:
        pixels[0]=(0, 255, 255)
        pixels.show()
        sleep(1)
        pixels[0] =(0, 0, 0)  


