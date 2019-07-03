from machine import Pin,TouchPad
from time import sleep
import neopixel

TPIN = 15 # タッチセンサにするピン
touch = TouchPad(Pin(TPIN))

def light(np,r,g,b):
    n = np.n
    np.fill((0,0,0))
    np.write()
    sleep(0.5)
    for i in range(n):
        np[i] = (r,g,b)
        np.write()
        sleep(0.5)


def run():
    touch = TouchPad(Pin(TPIN))
    np = neopixel.NeoPixel(Pin(13), 20, timing = 1)
    #sw1 = Pin(23,Pin.IN,Pin.PULL_UP)
    #sw2 = Pin(22,Pin.IN,Pin.PULL_UP)
    while True:
        if touch.read() <=800:
            light(np, 255,255,0)
        else:
            light(np, 0,255,0)
        #np.fill((0,0,0))
        np.write()
run()
