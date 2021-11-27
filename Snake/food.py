class Food():
    def __init__(self, width,height,x,y):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def generate_at(self,x,y):
        self.x = x
        self.y = y

    def coords(self):
        return (self.x,self.y)

