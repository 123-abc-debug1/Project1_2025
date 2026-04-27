from machine import Pin
from time import sleep
from random import uniform  # 新增这行

# Initialize LED
led = Pin(4, Pin.OUT)

# Test LED: random delay between 5-10 seconds
led.value(1)
sleep(uniform(5, 10))  # 修改这行
led.value(0)
