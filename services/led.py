import RPi.GPIO as GPIO
import time

class led:

	GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(18,GPIO.OUT)

	def turnRedOn(self):
		GPIO.output(18,GPIO.HIGH)

	def turnRedOff(self):
		GPIO.output(18,GPIO.LOW)
