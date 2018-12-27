from services.arduino import arduino

class actionHandler:

    def __init__(self):
        self.arduino = arduino()


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
