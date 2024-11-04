import os
import time
from gpiozero import LED

green = LED(24)
yellow = LED(23)
red = LED(18)

os.system("clear")

print("Choose what light (number) you would like to blink:")
print("1: Green")
print("2: Yellow")
print("3: Red")

user_input = int(input(""))

if user_input == 1:
    light = green
elif user_input == 2:
    light = yellow
elif user_input == 3:
    light = red
else:
    print("Invalid number choosen, program terminated") 

print("How many times would you like the light to blink?")
blinks = int(input(""))
print(f"Light will blink {blinks} of times")

if blinks > 0:
    while blinks > 0:
        light.on()
        time.sleep(1)
        light.off()    
        time.sleep(1)
        blinks -= 1


