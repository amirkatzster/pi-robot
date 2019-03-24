from services.arduino import arduino
from services.light import light
from services.spotify import spotify
from colour import Color
import json
from google.protobuf.json_format import MessageToJson
from numpy import interp

class actionHandler:

    def __init__(self):
        self.arduino = arduino()
        self.light = light()
        self.spotify = spotify()


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
        if actionName == "Sing":
            param = json.loads(params)
            querySong = param['parameters']['song']
            self.spotify.play(querySong) 
        if actionName == "MoveFw":
            self.arduino.send(71)
        if actionName == "MoveBw":
            self.arduino.send(72)
        if actionName == "TurnRight":
            self.arduino.send(73)
        if actionName == "TurnLeft":
            self.arduino.send(74)
        if actionName == "Stop":
            self.arduino.send(75)
        if actionName == "Test":
            self.arduino.send(256)
            

    def mapColor(self,color):
        return round(interp(color,[0.0,1.0],[1,255]))
