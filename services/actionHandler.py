from services.arduino import arduino

class actionHandler:

    def __init__(self):
        self.arduino = arduino()


    def process(self, actionName, params):
        if actionName == "Read-book-action":
            print(actionName)
            print(params)
        if actionName == "SayYes":
	        self.arduino.sayYes()
        if actionName == "SayNo":
            self.arduino.sayNo()
