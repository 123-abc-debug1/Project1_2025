from machine import Pin
from time import sleep
from random import uniform
import sys  # 新增这行

# Initialize components
led = Pin(4, Pin.OUT)
left_button = Pin(14, Pin.IN, Pin.PULL_UP)  # 新增这行
right_button = Pin(15, Pin.IN, Pin.PULL_UP)  # 新增这行

# Core game logic
led.value(1)
sleep(uniform(5, 10))
led.value(0)

# Wait for button press
while True:
    if left_button.value() == 0:
        print("Left button pressed!")
        sys.exit()
    if right_button.value() == 0:
        print("Right button pressed!")
        sys.exit()
