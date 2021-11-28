import pygame
from settings import MainSettings,PlayerSettings,ScreenSettings

class Player():
    def __init__(self):
        self.screenSettings = ScreenSettings()
        self.playerSettings = PlayerSettings()
        self.mainSettings = MainSettings()
        self.step = self.screenSettings.UNIT_SIDE
        self.x = 0 
        self.y = 0
        self.x_modifier = 1 * self.step
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

    def draw(self,screen): 
        pygame.draw.rect(screen, self.playerSettings.COLOR,(self.x,self.y,self.screenSettings.UNIT_SIDE,self.screenSettings.UNIT_SIDE),1)

    def move_up(self):
        self.x_modifier = 0
        self.y_modifier = -1 * self.screenSettings.UNIT_SIDE

    def move_down(self):
        self.x_modifier = 0
        self.y_modifier = 1 * self.screenSettings.UNIT_SIDE

    def move_left(self):
        self.x_modifier = -1 * self.screenSettings.UNIT_SIDE
        self.y_modifier = 0

    def move_right(self):
        self.x_modifier = 1 * self.screenSettings.UNIT_SIDE
        self.y_modifier = 0

    def display_info(self,screen):
        font = pygame.font.SysFont(self.mainSettings.FONT, self.mainSettings.FONT_SIZE)
        text = font.render(str(f'x:{self.x} y:{self.y}'), True, self.mainSettings.FONT_COLOR)
        screen.blit(text, (0,0))