from sense_hat import SenseHat
import time

sense = SenseHat()

c = [[0,255,255],
    [3, 23, 252],
    [3, 23, 252],
    [3, 23, 252],
    [3, 23, 252],
    [255,255,255],
    [3, 23, 252],
    [3, 23, 252],
    [3, 23, 252],
    [3, 23, 252],
    [255,255,255],
    [3, 23, 252],
    [3, 23, 252],
    [3, 23, 252],
    [3, 23, 252]]

mark=[[]*3]*64


def asigna_color(n):                            #n es el frame que se pide
    mark[0]=c[n]                                #ponemos en la esquina el color n que nos dice la función
    for i in range(1,64):                       #recorremos todos los leds menos el 0
        mark[i]=c[((i-7*int(i/8))%15+n)%15]
    return mark

while True:
    for k in range(15):
        #print("k=",k)
        sense.set_pixels(asigna_color(k))
        time.sleep(0.3)