import os
import time
from gpiozero import Buzzer, LED

buzzer = Buzzer(22)
led = LED(18)
unit = 0.2
space_between_letter = unit * 3
space_words = unit * 7

def dot():
    buzzer.on()
    led.on()
    time.sleep(unit)
    buzzer.off()
    led.off()

def dash():
    buzzer.on()
    led.on()
    time.sleep(unit * 3)
    buzzer.off()
    led.off()

morsecode = {
    "A": [dot, dash],
    "B": [dash, dot, dot],
    "C": [dash, dot, dash, dot],
    "D": [dash, dot, dot],
    "E": [dot],
    "F": [dot, dot, dash, dot],
    "G": [dash, dash, dot],
    "H": [dot, dot, dot, dot],
    "I": [dot, dot],
    "J": [dot, dash, dash, dash],
    "K": [dash, dot, dash],
    "L": [dot, dash, dot, dot],
    "M": [dash, dash],
    "N": [dash, dot],
    "O": [dash, dash, dash],
    "P": [dot, dash, dash, dot],
    "Q": [dash, dash, dot, dash],
    "R": [dot, dash, dot],
    "S": [dot, dot, dot], 
    "T": [dash],
    "U": [dot, dot, dash],
    "V": [dot, dot, dot, dash],
    "W": [dot, dash, dash],
    "X": [dash, dot, dot, dash],
    "Y": [dash, dot, dash, dash],
    "Z": [dash, dash, dot, dot],
    "0": [dash, dash, dash, dash, dash],
    "1": [dot, dash, dash, dash, dash],
    "2": [dot, dot, dash, dash, dash],
    "3": [dot, dot, dot, dash, dash],
    "4": [dot, dot, dot, dot, dash],
    "5": [dot, dot, dot, dot, dot],
    "6": [dash, dot, dot, dot, dot],
    "7": [dash, dash, dot, dot, dot],
    "8": [dash, dash, dash, dot, dot],
    "9": [dash, dash, dash, dash, dot]
}

userinput = "help me".upper()

for letter in userinput:
    if letter == " ":
        print("there is a space here")
        time.sleep(space_words)
    elif letter in morsecode:
        for call_function in morsecode[letter]:
            call_function()
            time.sleep(space_between_letter)
    else:
        print("Symbol unsupported, skipped")
