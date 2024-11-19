import os
from gpiozero import Button, Buzzer, LED
import time

LIGHTS = {
    "green": LED(24),
    "yellow": LED(23),
    "red": LED(18)
}

BUZZER = Buzzer(22)

class TrafficLight():
    def __init__(self, lights, buzzer):
        self.vehicle_lights = lights
        self.pedestrian_lights = lights
        self.buzzer = buzzer

    def lights_off(self):
        for light in self.vehicle_lights:
            self.vehicle_lights[light].off() 
        for light in self.pedestrian_lights:
            self.pedestrian_lights[light].off()

    def flash_lights(self, light, interval, repeat):
        count = 0
        while count <= repeat:
            light.on()
            time.sleep(interval / 2)
            light.off()
            time.sleep(interval / 2)
            count += 1

    def default_lights(self):
        self.vehicle_lights["green"].on()
        self.pedestrian_lights["red"].on()
        time.sleep(1)
        self.lights_off()

    def pedestrian_push(self):
        print("Pedestrian has pushed button")
        self.vehicle_lights["yellow"].on()
        self.pedestrian_lights["red"].on()
        time.sleep(3)
        self.lights_off()
    
        self.vehicle_lights["red"].on()
        self.pedestrian_lights["red"].on()
        time.sleep(1)
        self.lights_off()
    
    def pedestrian_walk(self):
        
        self.lights_off()
        self.vehicle_lights["red"].on()
        self.pedestrian_lights["green"].on()

        crossingTime = 5.0
        count = 0
        while count <= crossingTime:
            self.buzzer.on()
            time.sleep(0.5)
            self.buzzer.off()
            time.sleep(0.5)
            count += 1

        self.lights_off()

    def pedestrian_stop_walk(self):
        self.vehicle_lights["red"].on()
        self.flash_lights(self.pedestrian_lights["green"], 0.25, 4)
        
        self.flash_lights(self.vehicle_lights["yellow"], 0.25, 12)
        
    
def main(): 
    trafficLights = TrafficLight(LIGHTS, BUZZER)
    # trafficLights.default_lights()
    # trafficLights.pedestrian_push()
    # trafficLights.pedestrian_walk()
    # trafficLights.pedestrian_walk()
    trafficLights.pedestrian_stop_walk()

main()