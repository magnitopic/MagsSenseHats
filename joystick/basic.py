from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

while True:
	event = sense.stick.wait_for_event()
	print(f"The joystick was {event.action} {event.direction}")
	sleep(0.3)
	event = sense.stick.wait_for_event()
	print(f"The joystick was {event.action} {event.direction}")