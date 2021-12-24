import pygame
import time
from food import Food
from snake import Snake
from settings import MainSettings,ScreenSettings,GameSettings

screenSettings = ScreenSettings()
mainSettings = MainSettings()
gameSettings = GameSettings()

# Initial configurations
pygame.display.set_caption("Snake.py")
screen = pygame.display.set_mode(screenSettings.SCREEN_SIZE)
pygame.init()

# Functions and class definitions

def show_score():
    font = pygame.font.SysFont(mainSettings.FONT, mainSettings.FONT_SIZE)
    text = font.render(str(f'Score:{gameSettings.score}'), True, mainSettings.FONT_COLOR)
    screen.blit(text,(0,0))

snake = Snake(screenSettings.UNIT_SIDE*5,screenSettings.UNIT_SIDE*5,True)
food = Food(True)

# Main game loop 

while not gameSettings.game_over:
    
    screen.fill(screenSettings.COLOR)
    show_score()
        
    snake.draw(screen)
    food.draw(screen)


    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                gameSettings.game_over = True
            
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                snake.move_down()
            
            if pygame.key.get_pressed()[pygame.K_UP]:
                snake.move_up()

            if pygame.key.get_pressed()[pygame.K_LEFT]:
                snake.move_left()

            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                snake.move_right()
    
        if event.type == pygame.QUIT:
            gameSettings.game_over = True
    
    if not snake.move():
        gameSettings.game_over = True
        
    
    head = snake.get_head()
    if(food.x == head.x and food.y == head.y):
        food.generate()
        gameSettings.score+=1
        snake.add_section()

    
    pygame.display.update()
    
    time.sleep(mainSettings.REFRESH_RATE)

    


     
