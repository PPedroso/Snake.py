import pygame
from settings import MainSettings,PlayerSettings,ScreenSettings


class Snake():
    snake = []
        
    def get_head(self):
        return self.snake[0]

    def get_tail(self):
        return self.snake[-1]
    
    def __init__(self,x,y,debug):
        self.snake.append(SnakeSection(x,y,debug))

    def move(self):
        for snake_section in self.snake:
            snake_section.move()
    
    def move_up(self):
        for snake_section in self.snake:
            snake_section.change_direction_up()

    def move_down(self):
        for snake_section in self.snake:
            snake_section.change_direction_down()

    def move_left(self):
        for snake_section in self.snake:
            snake_section.change_direction_left()

    def move_right(self):
        for snake_section in self.snake:
            snake_section.change_direction_right()

    def draw(self,screen):
        for snake_section in self.snake:
            snake_section.draw(screen)

    def add_section(self):
        
        head = self.get_head()
        tail = self.get_tail()

        snake_section = SnakeSection(tail.x - tail.x_modifier, tail.y - tail.y_modifier,False)
        snake_section.x_modifier =  head.x_modifier
        snake_section.y_modifier =  head.y_modifier

        self.snake.append(snake_section)

class SnakeSection():
    def __init__(self,x,y,debug):
        self.screenSettings = ScreenSettings()
        self.playerSettings = PlayerSettings()
        self.mainSettings = MainSettings()
        self.step = self.screenSettings.UNIT_SIDE
        self.x = x
        self.y = y
        self.x_modifier = 1 * self.step
        self.y_modifier = 0
        self.debug = debug
        self.delay = 0
        
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

    def change_direction_up(self):
        self.x_modifier = 0
        self.y_modifier = -1 * self.screenSettings.UNIT_SIDE

    def change_direction_down(self):
        self.x_modifier = 0
        self.y_modifier = 1 * self.screenSettings.UNIT_SIDE

    def change_direction_left(self):
        self.x_modifier = -1 * self.screenSettings.UNIT_SIDE
        self.y_modifier = 0

    def change_direction_right(self):
        self.x_modifier = 1 * self.screenSettings.UNIT_SIDE
        self.y_modifier = 0

    def draw(self,screen): 
        pygame.draw.rect(screen, self.playerSettings.COLOR,(self.x,self.y,self.screenSettings.UNIT_SIDE,self.screenSettings.UNIT_SIDE),1,5)
        if self.debug:
            self.display_info(screen)
    
#Debug

    def display_info(self,screen):
        font = pygame.font.SysFont(self.mainSettings.DEBUG_FONT, self.mainSettings.DEBUG_FONT_SIZE)
        text = font.render(str(f'x:{self.x} y:{self.y}'), True, self.mainSettings.DEBUG_FONT_COLOR)
        screen.blit(text, (self.x + self.screenSettings.UNIT_SIDE,self.y- self.screenSettings.UNIT_SIDE))

    