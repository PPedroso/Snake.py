class MainSettings:
    def __init__(self):
        self.COLOR = (255,255,255)
        self.FONT = 'arial'
        self.FONT_SIZE = 25
        self.FONT_COLOR = (255,255,255)
        self.DEBUG_FONT = 'arial'
        self.DEBUG_FONT_SIZE = 10
        self.DEBUG_FONT_COLOR = (255,255,255)
        self.REFRESH_RATE = 0.05

class GameSettings:
    def __init__(self):
        self.game_over = False
        self.score = 0
        
class ScreenSettings:
    def __init__(self):
        self.UNIT_SIDE = 10
        self.UNIT_SIZE = (self.UNIT_SIDE,self.UNIT_SIDE)
        self.SCREEN_SIZE = (800,600)
        self.COLOR = (0,0,0)

class PlayerSettings:
    def __init__(self):
        self.COLOR = (0,255,0)
        self.INITIAL_SIZE = 4

class FoodSettings:
    def __init__(self):
        self.COLOR = (0,255,0)
