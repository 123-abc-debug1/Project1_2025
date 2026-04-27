from machine import Pin
from time import sleep

# Initialize LED
led = Pin(4, Pin.OUT)

# Test LED: on for 5 seconds then off
led.value(1)
sleep(5)
led.value(0)
