from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import os

sense = SenseHat()

def pushed_up(event):
	if event.action != ACTION_RELEASED:
		os.system("echo up")

def pushed_down(event):
	if event.action != ACTION_RELEASED:
		os.system("echo down")

def pushed_left(event):
	if event.action != ACTION_RELEASED:
		os.system("echo left")

def pushed_right(event):
	if event.action != ACTION_RELEASED:
		os.system("echo right")

def pushed_middle(event):
	if event.action != ACTION_RELEASED:
		os.system("echo middle")

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_middle = pushed_middle
pause()