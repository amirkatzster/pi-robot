from services.arduino import arduino
from services.light import light
from colour import Color
import json
from google.protobuf.json_format import MessageToJson
from numpy import interp

class actionHandler:

    def __init__(self):
        self.arduino = arduino()
	self.light = light()


    def process(self, actionName, params):
        if actionName == "Read-book-action":
            print(actionName)
            print(params)
        if actionName == "SayYes" or actionName == 'smalltalk.confirmation.yes':
	    self.arduino.sayYes()
        if actionName == "SayNo" or actionName == 'smalltalk.confirmation.no':
            self.arduino.sayNo()
	if actionName == "RaiseRightHand":
	    self.arduino.RaiseRightHand()
	if actionName == "LookRight":
	    self.arduino.send(2)
	if actionName == "LookLet":
            self.arduino.send(3)
	if actionName == "RaiseLeftHand":
            self.arduino.send(51)
	if actionName == "RaiseBothHands":
            self.arduino.send(52)
	if actionName == "HoldSomethingHands":
            self.arduino.send(53)
	if actionName == "TurnLightOn":
            self.light.turnOn()
	if actionName == "TurnLightOff":
	    self.light.turnOff()
	if actionName == "TurnLightColor":
	    param = json.loads(params)
            c = Color(param['parameters']['color'])
            self.light.turnOn()
            print(c.rgb)
	    print(self.mapColor(c.red),self.mapColor(c.green),self.mapColor(c.blue))
            #self.light.set_hsv(c.hue, c.saturation, c.luminance)
	    self.light.setColor(self.mapColor(c.red),self.mapColor(c.green),self.mapColor(c.blue))



    def mapColor(self,color):
        return round(interp(color,[0.0,1.0],[1,255]))
