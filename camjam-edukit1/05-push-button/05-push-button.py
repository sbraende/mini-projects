import os 
import time
from gpiozero import Button

button = Button(25)

while True:
    if (button.is_pressed):
        print("Button is pressed")
        time.sleep(1)
    else:
        os.system("clear")
        print("Waiting for you to press button...")
        
    time.sleep(0.5)