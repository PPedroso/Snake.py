import pygame
import random


screen_size = (800,600)

# Initial configurations
pygame.display.set_caption("Snake.py")
color = (255,255,255)
rectangle = pygame.Rect(5,5,60,60)
screen = pygame.display.set_mode(screen_size)
pygame.init()
game_over = False
GREEN = (0,255,0)
UNIT_SIZE = (10,10)


# Functions and class definitioNs
class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square,self).__init__()
        self.surface = pygame.Surface(UNIT_SIZE)
        self.rectangle = self.surface.get_rect()

def draw_at(x,y):
    pygame.draw.rect(screen,GREEN,(x,y,10,10),1);

# Main game loop

class Position():
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

class Food():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.generate()

    def generate(self):
        self.x = random.randint(0,screen_size[0])
        self.y = random.randint(0,screen_size[1])
        self.draw()
    
    def draw(self):
        draw_at(self.x,self.y)



   
pos = Position()
food = Food()

while not game_over:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                game_over = True
            
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                pos.x_modifier = 0
                pos.y_modifier = 1
            
            if pygame.key.get_pressed()[pygame.K_UP]:
                pos.x_modifier = 0
                pos.y_modifier = -1

            if pygame.key.get_pressed()[pygame.K_LEFT]:
                pos.x_modifier = -1
                pos.y_modifier = 0

            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                pos.x_modifier = 1
                pos.y_modifier = 0
        
        if event.type == pygame.QUIT:
            game_over = True


    draw_at(pos.x,pos.y)
    pos.move()
    
    if(food.x == pos.x and food.y == pos.y):
        food.generate()

    food.draw()
      

    pygame.display.update()

    


     
