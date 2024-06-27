class Mammals:
    def __init__(self):
        pass
    def heart(self):
        print("Four chamber heart")
class Human(Mammals):
    def brain(self):
        print("high thinking capacity")
class Jackle(Mammals):
    def brain(self):
        print("low compare to human")
        
class Cat(Mammals):
    def brain(self):
        print("low compare to jackle")

h=Human()
h.heart()
h.brain()
c=Cat()
c.heart()
c.brain()
j=Jackle()
j.brain()
j.heart()
