# coding=utf-8
from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

c = [[158, 255, 0],
    [158, 255, 0],
    [50, 255, 0],
    [0, 255, 71],
    [0, 255, 178],
    [0, 209, 255],
    [0, 86, 255],
    [20, 0, 255],
    [127, 0, 255],
    [249, 0, 255],
    [255, 0, 152],
    [255, 0, 45],
    [255, 61, 0],
    [255, 168, 0],
    [234, 255, 0]]

mark=[[]*3]*64 # 3 for the rgb, times total number of 


def asigna_color(n):                            #n is the colour the first led should be
    mark[0]=c[n]                                #we set the corner colour as the n value from our list
    for i in range(1,64):                       #we cycle through all the leds except 0
        mark[i]=c[((i-7*int(i/8))%15+n)%15]
    return mark

while True:
    for k in range(15):							#we do this 15 times so the corner changes between all 15 colours
        #print("k=",k)
        sense.set_pixels(asigna_color(k))
        time.sleep(0.2)