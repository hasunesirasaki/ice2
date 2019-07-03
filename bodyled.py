from machine import Pin
from time import sleep_ms
import neopixel

def light(np,r,g,b):
    n = np.n
    np.fill((0,0,0))
    np.write()
    sleep_ms(500)
    for i in range(n):
        np[i] = (r,g,b)
        np.write()
        sleep_ms(50)


def run():
    np = neopixel.NeoPixel(Pin(13), 20, timing = 1)
    sw1 = Pin(23,Pin.IN,Pin.PULL_UP)
    sw2 = Pin(22,Pin.IN,Pin.PULL_UP)
    while True:
        if sw1.value() ==0:
            light(np, 255,0,0)
        if sw2.value() ==0:
            light(np, 0,255,0)
        #np.fill((0,0,0))
        np.write()

run()
