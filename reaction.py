# Add reaction time calculation feature
from machine import Pin
from time import sleep, time
from random import uniform
import sys
...

# Initialize components (pin definitions match the assignment PDF exactly)
led = Pin(4, Pin.OUT)
left_button = Pin(14, Pin.IN, Pin.PULL_UP)
right_button = Pin(15, Pin.IN, Pin.PULL_UP)

# Get player names (required by the assignment)
left_name = input('left player name is ')
right_name = input('right player name is ')

print("\nGame about to start...")
print("LED is on, waiting for it to turn off...")

# Core game logic: LED on → random 5-10s delay → LED off (assignment specified rule)
led.value(1)
sleep(uniform(5, 10))
led.value(0)
led_off_time = time()  # Record LED off time (enhancement feature)

print("\nLED is off! Press the button quickly!")

# Wait for button press and determine winner
while True:
    if left_button.value() == 0:  # Pull-up resistor, low level when pressed
        reaction_time = round((time() - led_off_time) * 1000, 1)
        print(f"\n🎉 {left_name} won the game!")
        print(f"Reaction time: {reaction_time} ms")
        sys.exit()
    if right_button.value() == 0:
        reaction_time = round((time() - led_off_time) * 1000, 1)
        print(f"\n🎉 {right_name} won the game!")
        print(f"Reaction time: {reaction_time} ms")
        sys.exit()
# Fix button detection bug
