from machine import Pin
from time import sleep, time  # 新增time导入
from random import uniform
import sys

# Initialize components
led = Pin(4, Pin.OUT)
left_button = Pin(14, Pin.IN, Pin.PULL_UP)
right_button = Pin(15, Pin.IN, Pin.PULL_UP)

# Get player names
left_name = input('left player name is ')
right_name = input('right player name is ')

print("\nGame about to start...")
print("LED is on, waiting for it to turn off...")

# Core game logic
led.value(1)
sleep(uniform(5, 10))
led.value(0)
led_off_time = time()  # 新增：记录LED熄灭时间

print("\nLED is off! Press the button quickly!")

# Wait for button press and determine winner
while True:
    if left_button.value() == 0:
        reaction_time = round((time() - led_off_time) * 1000, 1)  # 新增：计算反应时间
        print(f"\n🎉 {left_name} won the game!")
        sys.exit()
    if right_button.value() == 0:
        reaction_time = round((time() - led_off_time) * 1000, 1)  # 新增：计算反应时间
        print(f"\n🎉 {right_name} won the game!")
        sys.exit()
