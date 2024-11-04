import time
from gpiozero import LED

green = LED(24)
yellow = LED(23)
red = LED(18)

while True:
    green.on()
    yellow.on()
    red.on()

    time.sleep(1)

    green.off()
    yellow.off()
    red.off()

    time.sleep(1)