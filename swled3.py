from machine import Pin
from time import sleep
import random, neopixel

maxlen = 20
neo = neopixel.NeoPixel(Pin(13), maxlen,timing=1)
def main():
    for i in range(maxlen):
        r = random.randrange(255)
        g = random.randrange(255)
        b = random.randrange(255)
        neo[i] = (r,g,b)
    neo.write()
    sleep(1)
while True:
    main()
    main()
    main()
