from sense_hat import SenseHat
import time

sense = SenseHat()

c = [[255,0,0],
    [255,102,0],
    [255,153,51],
    [255,102,153],
    [204,153,255],
    [102,102,255],
    [0,0,255],
    [0,153,255],
    [0,255,255],
    [255,204,0],
    [102,255,51],
    [204,255,51],
    [255,255,0],
    [255,204,0],
    [255,51,0]]

mark=[[]*3]*64


def asigna_color(n):                #n es el frame que se pide
    mark[n]=c[n]
    for i in range(1,64):           #i es columnas
        if i%8!=0:
            print("i general=",i)
            mark[i]=c[(i-7)%15]
        else:
            mark[i]=c[i%15]
            print("i particular =",i)
    return mark

while True:
    for k in range(15):
        print("k=",k)
        sense.set_pixels(asigna_color(k))
        time.sleep(1)