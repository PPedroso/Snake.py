class MainSettings:
    def __init__(self):
        self.COLOR = (255,255,255)
        self.FONT = 'arial'
        self.FONT_SIZE = 15
        self.FONT_COLOR = (255,255,255)

class GameSettings:
    def __init__(self):
        self.game_over = False
        self.score = 0
        
class ScreenSettings:
    def __init__(self):
        self.UNIT_SIDE = 10
        self.UNIT_SIZE = (self.UNIT_SIDE,self.UNIT_SIDE)
        self.SCREEN_SIZE = (800,600)

class PlayerSettings:
    def __init__(self):
        self.COLOR = (255,255,0)

class FoodSettings:
    def __init__(self):
        self.COLOR = (255,0,0)
