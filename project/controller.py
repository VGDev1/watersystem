from gpiozero import *
import RPi.GPIO as GPIO
import time

class Controller:

    def __init__(self, setTime):
        self.setTime = int(setTime)*60
        self.run = False
        GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
        self.RELAY1 = 4
        self.RELAY2 = 27
        self.RELAY3 = 22
        self.RELAY4 = 17
        self.RELAY5 = 23
        GPIO.setup(self.RELAY1, GPIO.OUT) # GPIO Assign mode
        GPIO.setup(self.RELAY2, GPIO.OUT) # GPIO Assign mode
        GPIO.setup(self.RELAY3, GPIO.OUT) # GPIO Assign mode
        GPIO.setup(self.RELAY4, GPIO.OUT) # GPIO Assign mode
        GPIO.setup(self.RELAY5, GPIO.OUT) # GPIO Assign mode
        self.deactivateWater()
    
    def activateWater(self):
        self.run = True
        startTime = time.time()
        sequences = []
        for i in range(1, 6):
            sequences.append(self.setTime/5 * i)
        while self.run:
            print(sequences[0], sequences[1], sequences[2], sequences[3], sequences[4])
            currentTime = time.time() - startTime
            if currentTime < sequences[0]:
                print("turn on group A")
                GPIO.output(self.RELAY1, GPIO.LOW) # on
                GPIO.output(self.RELAY2, GPIO.HIGH) # on
                GPIO.output(self.RELAY3, GPIO.HIGH) # on
                GPIO.output(self.RELAY4, GPIO.HIGH) # on
                GPIO.output(self.RELAY5, GPIO.HIGH) # on
            elif currentTime < sequences[1]:
                print("turn on group B")
                GPIO.output(self.RELAY1, GPIO.HIGH) # on
                GPIO.output(self.RELAY2, GPIO.LOW) # on
                GPIO.output(self.RELAY3, GPIO.HIGH) # on
                GPIO.output(self.RELAY4, GPIO.HIGH) # on
                GPIO.output(self.RELAY5, GPIO.HIGH) # on
            elif currentTime < sequences[2]:
                print("turn on group C")
                GPIO.output(self.RELAY1, GPIO.HIGH) # on
                GPIO.output(self.RELAY2, GPIO.HIGH) # on
                GPIO.output(self.RELAY3, GPIO.LOW) # on
                GPIO.output(self.RELAY4, GPIO.HIGH) # on
                GPIO.output(self.RELAY5, GPIO.HIGH) # on
            elif currentTime < sequences[3]:
                print("turn on group D")
                GPIO.output(self.RELAY1, GPIO.HIGH) # on
                GPIO.output(self.RELAY2, GPIO.HIGH) # on
                GPIO.output(self.RELAY3, GPIO.HIGH) # on
                GPIO.output(self.RELAY4, GPIO.LOW) # on
                GPIO.output(self.RELAY5, GPIO.HIGH) # on
            elif currentTime < sequences[4]:
                print("turn on group E")
                GPIO.output(self.RELAY1, GPIO.HIGH) # on
                GPIO.output(self.RELAY2, GPIO.HIGH) # on
                GPIO.output(self.RELAY3, GPIO.HIGH) # on
                GPIO.output(self.RELAY4, GPIO.HIGH) # on
                GPIO.output(self.RELAY5, GPIO.LOW) # on
            else:
                self.deactivateWater()
            time.sleep(10)

    def deactivateWater(self):
        self.run = False
        GPIO.output(self.RELAY1, GPIO.HIGH) # on
        GPIO.output(self.RELAY2, GPIO.HIGH) # on
        GPIO.output(self.RELAY3, GPIO.HIGH) # on
        GPIO.output(self.RELAY4, GPIO.HIGH) # on
        GPIO.output(self.RELAY5, GPIO.HIGH) # on
        # Some code here setting the realys low
