from machine import Pin
from time import sleep
from random import uniform
import sys

# Initialize components
led = Pin(4, Pin.OUT)
left_button = Pin(14, Pin.IN, Pin.PULL_UP)
right_button = Pin(15, Pin.IN, Pin.PULL_UP)

# Get player names
left_name = input('left player name is ')  # 新增这行
right_name = input('right player name is ')  # 新增这行

print("\nGame about to start...")
print("LED is on, waiting for it to turn off...")

# Core game logic
led.value(1)
sleep(uniform(5, 10))
led.value(0)

print("\nLED is off! Press the button quickly!")

# Wait for button press and determine winner
while True:
    if left_button.value() == 0:
        print(f"\n🎉 {left_name} won the game!")  # 修改这行
        sys.exit()
    if right_button.value() == 0:
        print(f"\n🎉 {right_name} won the game!")  # 修改这行
        sys.exit()
