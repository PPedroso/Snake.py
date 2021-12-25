import random
import pygame

from settings import FoodSettings,ScreenSettings,MainSettings

class Food():
    def __init__(self,debug):
        self.screenSettings = ScreenSettings()
        self.foodSettings = FoodSettings()
        self.mainSettings = MainSettings()
        self.debug = debug
        self.generate()

    def generate(self):

        self.x = self.screenSettings.UNIT_SIDE * random.randint(0, (self.screenSettings.SCREEN_SIZE[0] - self.screenSettings.UNIT_SIDE) / (self.screenSettings.UNIT_SIDE))
        self.y = self.screenSettings.UNIT_SIDE * random.randint(0, (self.screenSettings.SCREEN_SIZE[1] - self.screenSettings.UNIT_SIDE) / (self.screenSettings.UNIT_SIDE))
        
    def draw(self,screen):
        pygame.draw.rect(screen,self.foodSettings.COLOR,(self.x,self.y,self.screenSettings.UNIT_SIDE,self.screenSettings.UNIT_SIDE),0,1)

        if self.debug:
            self.display_info(screen)

#Debug
    def display_info(self,screen):
        font = pygame.font.SysFont(self.mainSettings.DEBUG_FONT, self.mainSettings.DEBUG_FONT_SIZE)
        text = font.render(str(f'x:{self.x} y:{self.y}'), True, self.mainSettings.DEBUG_FONT_COLOR)
        screen.blit(text, (self.x + self.screenSettings.UNIT_SIDE,self.y- self.screenSettings.UNIT_SIDE))


