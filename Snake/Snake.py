import pygame
from settings import MainSettings,PlayerSettings,ScreenSettings


class Snake():
    snake = []
        
    def __init__(self,x,y,debug):
        self.snake.append(SnakeSection(x,y,debug))
        
        for i in range(0,PlayerSettings().INITIAL_SIZE):
            self.add_section()
    
    def get_head(self):
        return self.snake[0]

    def get_tail(self):
        return self.snake[-1]

    def move(self):
        head = self.get_head()
        head.move()

        if(head.x) > ScreenSettings().SCREEN_SIZE[0] or (head.x) < 0:
            return False
        if(head.y) > ScreenSettings().SCREEN_SIZE[1] or (head.y) < 0:
            return False

        for snake_section in self.snake[1:]:
            if snake_section.x == head.x and snake_section.y == head.y:
                return False
            snake_section.move()

        for i in range(len(self.snake)-1,0,-1):
            if i > 0:
                self.snake[i].x_modifier = self.snake[i-1].x_modifier
                self.snake[i].y_modifier = self.snake[i-1].y_modifier
        return True
    
    def move_up(self):
        self.get_head().change_direction_up()

    def move_down(self):
        self.get_head().change_direction_down()

    def move_left(self):
        self.get_head().change_direction_left()

    def move_right(self):
        self.get_head().change_direction_right()

    def draw(self,screen):
        for snake_section in self.snake:
            snake_section.draw(screen)

    def add_section(self):
        tail = self.get_tail()

        snake_section = SnakeSection(tail.x - tail.x_modifier, tail.y - tail.y_modifier,False)
        snake_section.x_modifier =  tail.x_modifier
        snake_section.y_modifier =  tail.y_modifier

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

    def change_direction_up(self):
        if(self.x_modifier == 0):
            return
        
        self.x_modifier = 0
        self.y_modifier = -1 * self.screenSettings.UNIT_SIDE

    def change_direction_down(self):
        if(self.x_modifier == 0):
            return
        
        self.x_modifier = 0
        self.y_modifier = 1 * self.screenSettings.UNIT_SIDE

    def change_direction_left(self):
        if(self.y_modifier == 0):
            return
        
        self.x_modifier = -1 * self.screenSettings.UNIT_SIDE
        self.y_modifier = 0

    def change_direction_right(self):
        if(self.y_modifier == 0):
            return

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

    