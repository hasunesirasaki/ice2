from machine import Pin
from time import sleep
import random, neopixel
maxlen = 10
neo = neopixel.NeoPixel(Pin(13), maxlen,timing=1)
sw=[]
for i in [5,18,19]:
    sw.append(Pin(i,Pin.IN,Pin.PULL_UP))

neo.fill((155,155,0))
neo.write
sleep(1)

def main():
    if sw[0].value()==0:
        neo.fill((255,255,0))
    if sw[1].value()==0:
        neo.fill((255,25,0))
    if sw[2].value()==0:
        neo.fill((255,55,0))
    neo.write()

while (True):
    main()
