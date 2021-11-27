import pygame
import time
import random
from food import Food
from player import Player


SCREEN_SIZE = (800,600)

# Initial configurations
pygame.display.set_caption("Snake.py")
color = (255,255,255)
square_size = (20,20)
rectangle = pygame.Rect(square_size[0],square_size[1],60,60)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.init()
game_over = False
YELLOW = (255,255,0)
UNIT_SIZE = (10,10)

# Functions and class definitions
def draw_at(x,y):
    pygame.draw.rect(screen,YELLOW,(x,y,square_size[0],square_size[1]),1)

 # Main game loop 

pos = Player()

x = square_size[0] * random.randint(0,SCREEN_SIZE[0] / square_size[0])
y = square_size[0] * random.randint(0,SCREEN_SIZE[1] / square_size[0])
food = Food(SCREEN_SIZE[0],SCREEN_SIZE[1],x,y)

while not game_over:

    screen.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                game_over = True
            
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                pos.x_modifier = 0
                pos.y_modifier = 1 * square_size[0]
            
            if pygame.key.get_pressed()[pygame.K_UP]:
                pos.x_modifier = 0
                pos.y_modifier = -1 * square_size[0]

            if pygame.key.get_pressed()[pygame.K_LEFT]:
                pos.x_modifier = -1 * square_size[0]
                pos.y_modifier = 0

            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                pos.x_modifier = 1 * square_size[0]
                pos.y_modifier = 0
        
        if event.type == pygame.QUIT:
            game_over = True


    draw_at(pos.x,pos.y)
    pos.move()
    
    if(food.x == pos.x and food.y == pos.y):
        x = square_size[0] * random.randint(0,SCREEN_SIZE[0] / square_size[0])
        y = square_size[0] * random.randint(0,SCREEN_SIZE[1] / square_size[0])
        food.generate_at(x,y)
    
    food_coords = food.coords()
    draw_at(food_coords[0],food_coords[1])

    font = pygame.font.SysFont('arial', 10)
    text = font.render(str(f'x:{pos.x} y:{pos.y} - player | x:{food_coords[0]} y:{food_coords[1]} - food'), True, YELLOW)
    screen.blit(text, (0,0))
    
    pygame.display.update()
    
    time.sleep(0.05)

    


     
