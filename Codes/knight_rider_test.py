import board
import neopixel
import time

# Define the number of NeoPixels and the GPIO pin
num_pixels = 60 # Change this to match the number of NeoPixels you are using
pixel_pin = board.D18  # Change this to match the GPIO pin you are using
ORDER = neopixel.RGBW

# Define the color of the LED pulse
color = (255, 0, 0, 0)  # Red, adjust as needed

# Define the delay time between each step of the pulse
delay = 0.01  # Adjust as needed

# Initialize the NeoPixel strip
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)

#test
#pixels.fill((0,0,0))
#pixels.show()
#sleep(1)

# bottom left = 96 bottom right = 0

#left = 48
#right  = 47

def pulse(color, num_pixels, delay):
    for i in range(num_pixels):
        pixels[i] = color
        pixels.show()
        time.sleep(delay)
        pixels.fill((0, 0, 0, 0))  # Turn off the pixel
        pixels.show()
        time.sleep(delay)

    for i in range(num_pixels-1, -1, -1):
        pixels[i] = color
        pixels.show()
        time.sleep(delay)
        pixels.fill((0, 0, 0, 0))  # Turn off the pixel
        pixels.show()
        time.sleep(delay)

try:
    while True:
        pulse(color, num_pixels, delay)
        

except KeyboardInterrupt:
    pixels.fill((0, 0, 0, 0))  # Turn off all pixels
    pixels.show()

