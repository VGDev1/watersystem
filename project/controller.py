from gpiozero import *
from time import *

class Controller:

    def __init__(self, setTime):
        self.setTime = setTime
        self.run = False
    
    def activateWater(self):
        self.run = True
        startTime = time.time()
        sequences = []
        for i in range(1, 7):
            sequences.append(self.setTime/6 * i)


        while self.run:
            currentTime = time.time() - startTime
            if(currentTime < self.setTime/)

