import board
import time
from random import randint
import neopixel

print("""Matrix

Follow the white rabbit...
""")

# Assuming you have the correct values for pixel_pin, num_pixels, and ORDER
pixel_pin = board.D18  # Replace with the correct pin number
num_pixels = 97  # Replace with the correct number of pixels
ORDER = neopixel.RGB  # Replace with the correct pixel order

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.1, auto_write=False, pixel_order=ORDER
)

wrd_rgb = [
    [154, 154, 173], [0, 0, 255], [0, 0, 200], [0, 0, 162],
    [0, 0, 145], [0, 0, 96], [0, 0, 174], [0, 0, 0]
]


clock = 0

blue_pilled_population = [[randint(0, 1), 7]]
while True:
    for person in blue_pilled_population:
        y = person[1]
        for rgb in wrd_rgb:
            if 0 <= y <= 8:
                pixels[person[0] + y * 8] = tuple(rgb)
            y += 1
        person[1] -= 1
    pixels.show()
    time.sleep(0.1)
    clock += 1
    if clock % 5 == 0:
        blue_pilled_population.append([randint(0, 7), 7])
    if clock % 7 == 0:
        blue_pilled_population.append([randint(0, 7), 7])
    while len(blue_pilled_population) > 100:
        blue_pilled_population.pop(0)

    # Assuming you want to clear the neopixel array
    pixels.fill((0, 0, 0))

    

    
