class Mammals:
    def __init__(self):
        pass
    def heart(self):
        print("Four chamber heart")
class Human(Mammals):
    def brain(self):
        print("high thinking capacity")
h=Human()
h.heart()
h.brain()