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
    np1 = neopixel.NeoPixel(Pin(13), 20, timing = 1)
    np2 = neopixel.NeoPixel(Pin(14), 20, timing = 1)
    sw1 = Pin(23,Pin.IN,Pin.PULL_UP)
    sw2 = Pin(22,Pin.IN,Pin.PULL_UP)
    while True:
        if sw1.value() ==0:
            light(np1, 255,255,0)#黄色
        if sw2.value() ==0:
            light(np2, 255,243,186)#白色
        #np.fill((0,0,0))
        np1.write()
        np2.write()

run()
