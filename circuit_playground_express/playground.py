"""This is the "Hello, world!" of CircuitPython: Blinky! This example blinks the little red LED on
and off!"""
import time
from adafruit_circuitplayground import cp

RED = (255, 0, 0)
BLUE = (0, 0, 255)

while True:
	for i in range(0, 10):
		cp.pixels[i] = RED
		time.sleep(0.5)

	time.sleep(0.5)

	for i in range(0, 10):
		cp.pixels[i] = BLUE
		time.sleep(0.5)

# cp.red_led
# cp.switch

########
# while True:
#   if cp.switch:
#     cp.red_led = True
#   else:
#     cp.red_led = False

########
# while True:
#     cp.red_led = not cp.switch

########
# cp.detect_taps = 2

# while True:
#   if cp.tapped:
#     cp.red_led = True
#   time.sleep(0.05)

########

# my_color = (0, 0, 255)

# while True:
#   cp.pixels.fill(my_color)

########

# cp.pixels.brightness = 1

# for i in range(10):
#   if i%2 == 0:
#     cp.pixels[i] = (255, 0, 0)
#   else:
#     cp.pixels[i] = (0, 255, 0)

#   time.sleep(0.5)

#%% ========== loop continue and break ========== %%#
import random

arr = [[random.randint(0,10) for _ in range(3)] for _ in range(10)]

for el in arr:
	for i in el:
		if i%10 == 0:
			break
		print(i)
