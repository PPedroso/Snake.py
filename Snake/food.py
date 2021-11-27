import random

class Food():
    def __init__(self, width,height):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height

        self.generate()

    def generate(self):
        self.x = random.randint(0,self.width)
        self.y = random.randint(0,self.height)

    def coords(self):
        return (self.x,self.y)

