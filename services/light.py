import time
from yeelight import Bulb


class light:
    
    def __init__(self):
        self.bulb = Bulb("192.168.0.102")
        print(1)
    
    def setColor(self,red,green,blue):
        self.bulb.set_rgb(red,green,blue)
        print(1)

    def turnOn(self):
        self.bulb.turn_on()
        print(1)
    
    def turnOff(self):
        self.bulb.turn_off()
        print(1)
    
    def start(self):
        print(2)
        #print(discover_bulbs())
        bulb = Bulb("192.168.0.102")
        for r in range(1,256,40):
            for g in range(1,256,40):
                for b in range(1,256,40):
                    print('{} {} {}'.format(r,g,b))
                    bulb.set_rgb(r, g, b)
                    time.sleep(1)


