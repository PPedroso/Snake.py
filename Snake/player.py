class Player():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.x_modifier = 0
        self.y_modifier = 0
    def move(self):
        self.x += self.x_modifier
        self.y += self.y_modifier
        if(self.x) > 800:
            self.x = 0
        if(self.y) > 600:
            self.y = 0
        if(self.x) < 0:
            self.x = 800
        if(self.y) < 0:
            self.y = 600