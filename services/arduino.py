
#import RPi.GPIO as gpio
import smbus
import time
import sys


class arduino:

    def __init__(self):
        self.bus = smbus.SMBus(1)
        self.address = 0x04

    def send(self, num):
	self.bus.write_byte(self.address, num)
##### Head ########
    def sayNo(self):
        #gpio.output(17, True)
        print('going to say no')
        self.bus.write_byte(self.address, 2)
	print('saying no')

    def sayYes(self):
        self.bus.write_byte(self.address, 1)

    def LookRight(self):
        self.bus.write_byte(self.address, 3)

    def LookLeft(self):
        self.bus.write_byte(self.address, 4)

    def Search(self):
        self.bus.write_byte(self.address, 5)

##### Hands ########
    def RaiseRightHand(self):
        self.bus.write_byte(self.address, 50)

    def RaiseLeftHand(self):
        self.bus.write_byte(self.address, 51)

    def RaiseBothHands(self):
        self.bus.write_byte(self.address, 52)

    def HoldSomethingHands(self):
        self.bus.write_byte(self.address, 53)

    def KifHands(self):
        self.bus.write_byte(self.address, 54)

###### Drive #######
    def DriveFw(self):
        self.bus.write_byte(self.address, 80)

    def DriveBw(self):
        self.bus.write_byte(self.address, 81)

    def TurnRight(self):
        self.bus.write_byte(self.address, 82)

    def TurnLeft(self):
        self.bus.write_byte(self.address, 83)        

    
