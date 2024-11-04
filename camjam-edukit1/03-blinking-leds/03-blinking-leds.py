import time
from gpiozero import LED

green = LED(24)
yellow = LED(23)
red = LED(18)

lights = [green, yellow, red]

while True:
    for light in lights: 
        light.on()
    
    time.sleep(1)

    for light in lights:
        light.off()
    
    time.sleep(1)