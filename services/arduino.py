
#import RPi.GPIO as gpio
import smbus
import time
import sys


class arduino:

    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.address = 0x04

    def sayYes(self):
        #gpio.output(17, True)
        print(self.address)
        print(self.bus)
        self.bus.write_byte(self.address, 1)
	print('saying yes')
        #time.sleep(1)

    def sayNo(self):
        #gpio.output(17, True)
	print('going to say no')
        self.bus.write_byte(self.address, 0)
	print('saying no')
        #time.sleep(1)
