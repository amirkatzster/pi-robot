
import RPi.GPIO as gpio
import smbus
import time
import sys


class arduino:

    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.address = 0x04
        gpio.setmode(gpio.BCM)
        gpio.setup(17, gpio.OUT)

    def sayYes(self):
        gpio.output(17, False)
        self.bus.write_byte(self.address, 1) 
        time.sleep(1)

    def sayNo(self):
        gpio.output(17, True)
        self.bus.write_byte(self.address, 0)     
        time.sleep(1)