import os
import time
from gpiozero import Buzzer, LED

class morsecode_generator():
    def __init__(self, buzzer_pin:int, led_pin:int):
        self.buzzer = Buzzer(buzzer_pin)
        self.led = LED(led_pin)
        self.unit = 0.2
        self.unit_dot = self.unit
        self.unit_dash = self.unit * 3
        self.space_between_parts_letters = self.unit
        self.space_between_letters = self.unit * 3
        self.space_words = self.unit * 7

        self.morsecode_table = {
            "A": ["dot", "dash"],
            "B": ["dash", "dot", "dot"],
            "C": ["dash", "dot", "dash", "dot"],
            "D": ["dash", "dot", "dot"],
            "E": ["dot"],
            "F": ["dot", "dot", "dash", "dot"],
            "G": ["dash", "dash", "dot"],
            "H": ["dot", "dot", "dot", "dot"],
            "I": ["dot", "dot"],
            "J": ["dot", "dash", "dash", "dash"],
            "K": ["dash", "dot", "dash"],
            "L": ["dot", "dash", "dot", "dot"],
            "M": ["dash", "dash"],
            "N": ["dash", "dot"],
            "O": ["dash", "dash", "dash"],
            "P": ["dot", "dash", "dash", "dot"],
            "Q": ["dash", "dash", "dot", "dash"],
            "R": ["dot", "dash", "dot"],
            "S": ["dot", "dot", "dot"], 
            "T": ["dash"],
            "U": ["dot", "dot", "dash"],
            "V": ["dot", "dot", "dot", "dash"],
            "W": ["dot", "dash", "dash"],
            "X": ["dash", "dot", "dot", "dash"],
            "Y": ["dash", "dot", "dash", "dash"],
            "Z": ["dash", "dash", "dot", "dot"],
            "0": ["dash", "dash", "dash", "dash", "dash"],
            "1": ["dot", "dash", "dash", "dash", "dash"],
            "2": ["dot", "dot", "dash", "dash", "dash"],
            "3": ["dot", "dot", "dot", "dash", "dash"],
            "4": ["dot", "dot", "dot", "dot", "dash"],
            "5": ["dot", "dot", "dot", "dot", "dot"],
            "6": ["dash", "dot", "dot", "dot", "dot"],
            "7": ["dash", "dash", "dot", "dot", "dot"],
            "8": ["dash", "dash", "dash", "dot", "dot"],
            "9": ["dash", "dash", "dash", "dash", "dot"]
        }

    def dot(self):
        self.buzzer.on()
        self.led.on()
        time.sleep(self.unit_dot)
        self.buzzer.off()
        self.led.off()

    def dash(self):
        self.buzzer.on()
        self.led.on()
        time.sleep(self.unit_dash)
        self.buzzer.off()
        self.led.off()

    def message(self):
        return input("Message to convert to morse code:").upper()

    def play(self, message):
        for symbol in message:
            if symbol in self.morsecode_table:
                time.sleep(self.space_between_letters)
                for value in self.morsecode_table[symbol]:
                    if value == "dot":
                        self.dot()
                    elif value == "dash":
                        self.dash()
                    time.sleep(self.space_between_parts_letters)
            elif symbol == " ":
                print("there is a space here")
                time.sleep(self.space_words)
            else:
                print("Symbol unsupported, skipped")
        print("Message done")

def main():
    moresecode = morsecode_generator(22, 18)
    message = moresecode.message()
    moresecode.play(message)
main()
