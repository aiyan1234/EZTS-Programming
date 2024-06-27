class Mammals:
    def __init__(self):
        pass
    def heart(self):
        print("Four chamber heart")
class Human(Mammals):
    def brain(self):
        print("high thinking capacity")
class Male(Human):
    def gender(self):
        print("Male is one of the gender out of two")
h=Human()
h.heart()
h.brain()
m=Male()
m.brain()
m.heart()
m.gender()
