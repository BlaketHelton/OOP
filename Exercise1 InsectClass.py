import random
'''
class Insect():
    def __init__(self, wings, legs):
        self.wings = wings
        self.legs = legs
    
    def lengthOfFlight(self):
        return random.randint(1, 10)

insect = Insect(2, 4)
print("The insect can fly " + str(insect.lengthOfFlight()) + " miles.")
'''
class Insect:
    def __init__(self):
        self.wings = 2
        self.legs = 4
        self.flight = 0

    def lengthOfFlight(self):
        return random.randint(1, 10)

    def get_flight(self):
        return Insect.lengthOfFlight


insect = Insect()
print("The insect can fly " + str(insect.lengthOfFlight()) + " miles.")
