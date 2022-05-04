from multiprocessing import Process
from sense_hat import SenseHat
import random, time

sense = SenseHat()
sense.clear()

def task():
	x=random.randrange(8)
	y=random.randrange(8)
	R=random.randrange(0,255)
	G=random.randrange(0,255)
	B=random.randrange(0,255)
	color=[random.randrange(256),random.randrange(256),random.randrange(256)]
	sense.set_pixel(x, y, R,G,B)
	time.sleep(.3)
	sense.set_pixel(x, y, 0,0,0)

max_processes = 10

while True:
	tasks = []
	# Run this task with max times
	for i in range(0, max_processes):
		tasks.append(task)

	all_processes = []

	for func in tasks:
		p = Process(target = func)
		all_processes.append(p)
		p.start()

	for p in all_processes:
		p.join()
