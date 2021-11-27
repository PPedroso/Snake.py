import pygame
from food import Food
from player import Player


SCREEN_SIZE = (800,600)

# Initial configurations
pygame.display.set_caption("Snake.py")
color = (255,255,255)
rectangle = pygame.Rect(5,5,60,60)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.init()
game_over = False
GREEN = (255,255,0)
UNIT_SIZE = (10,10)


# Functions and class definitions
class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square,self).__init__()
        self.surface = pygame.Surface(UNIT_SIZE)
        self.rectangle = self.surface.get_rect()

def draw_at(x,y):
    pygame.draw.rect(screen,GREEN,(x,y,10,10),1)



 # Main game loop 

pos = Player()
food = Food(SCREEN_SIZE[0],SCREEN_SIZE[1])

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
    
    food_coords = food.coords()
    draw_at(food_coords[0],food_coords[1])
    
    pygame.display.update()

    


     
