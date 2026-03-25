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


#left = 48
#right  = 47

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

    ''' test time
    hr = 19
    mins = int(45)
    sec = 43'''

    # SECONDS
    #pixels[47]=(255, 255, 0)

    # WORKS OUT HOURS
    #TimeLEDS = [0,  1,  2,  3,  4,  5, 6, 7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24] TIME
    TimeLEDS =  [47, 39, 31, 23, 15, 7, 0, 88, 80, 72, 64, 56, 48, 39, 31, 23, 15, 7,  96, 88, 80, 72, 64, 56, 48] #LED light to display in order of the hour position

    print ("Hours LED", TimeLEDS[hr-1]) #dAYLIGHT sAVING?'

    led_number = TimeLEDS[hr] #dAYLIGHT sAVING?'

    # left 12:00 = 47 and 48, 13:00 = 40, 14:00 = 32, 15:00 = 24, 16:00 = 16, 17:00 = 8, 18:00 = 0

    pixels[led_number]=(0, 255, 0)
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

    if sec == 0: # checks for new hour 00:00
        pixels[47]=(255, 255, 0)
        #pixels.show()
        pixels[48]=(255, 255, 0)
        pixels.show()
        sleep(1) # waits one second
        pixels[48] =(0, 0, 0) # clears the second LEDS from suit
        pixels[47] =(0, 0, 0)  
    if sec == 30: # checks for half past 30 mins
        pixels[96]=(255, 255, 0)
        #pixels.show()
        pixels[0]=(255, 255, 0)
        pixels.show()
        sleep(1)
        pixels[96] =(0, 0, 0)
        pixels[0] =(0, 0, 0)  
    elif sec < 30:
        #minuteLightPosition = mins * 1.6 - 1
        secLightPosition = 48 - (sec * 1.6) 
        print (secLightPosition)
        pixels[int(secLightPosition)]=(255, 255, 0)
        pixels.show()
        sleep(1)
        pixels[int(secLightPosition)] =(0, 0, 0)  
    elif mins > 30:
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

        


 
    

         
    
        
    #sleep(1) #wait 1 min before update MIGHT NEED TO MOVE
    #pixels.fill((0,0,0))    
    

    






'''
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
    sleep(0.2)  '''



#pixels[7]=((0, 255, 0))
#pixels.show()
#sleep(10)

