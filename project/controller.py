from gpiozero import *
import time

class Controller:

    def __init__(self, setTime):
        self.setTime = int(setTime)*60
        self.run = False
    
    def activateWater(self):
        self.run = True
        startTime = time.time()
        sequences = []
        for i in range(1, 5):
            sequences.append(self.setTime/4 * i)
        while self.run:
            print(sequences[0], sequences[1], sequences[2], sequences[3])
            currentTime = time.time() - startTime
            if currentTime < sequences[0]:
                print("turn on group A")
            elif currentTime < sequences[1]:
                print("turn on group B")
            elif currentTime < sequences[2]:
                print("turn on group C")
            elif currentTime < sequences[3]:
                print("turn on group D")
            else:
                self.run = False
            time.sleep(10)

    def deactivateWater(self):
        self.run = False
        # Some code here setting the realys low
