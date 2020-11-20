from sense_hat import SenseHat
import random
import time

sense = SenseHat()

while True:
    x=random.randrange(8)
    y=random.randrange(8)
    R=random.randrange(0,255)
    G=random.randrange(0,255)
    B=random.randrange(0,255)
    color=[random.randrange(256),random.randrange(256),random.randrange(256)]
    sense.set_pixel(x, y, R,G,B)