class Mammals:
    def __init__(self):
        pass
    def heart(self):
        print("Four chamber heart")
class Human:
    def brain(self):
        print("high thinking capacity")
    def gender(self):
        print("human has two genders")
class Male(Mammals,Human):
    def gender(self):
        print("Male is one of the gender out of two")

m=Male()
m.gender()
m.brain()
m.heart()
