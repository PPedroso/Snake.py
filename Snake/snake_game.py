import pygame
import time
from food import Food
from snake import SnakeSection
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
    screen.blit(text, (0,0))

player = SnakeSection(gameSettings.snake_pieces,screenSettings.UNIT_SIDE*5,screenSettings.UNIT_SIDE*5,True)
food = Food(True)

snake = [player]

# Main game loop 

while not gameSettings.game_over:

    screen.fill(screenSettings.COLOR)
    show_score()
    
    for bit in snake:
        bit.draw(screen)
    food.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                gameSettings.game_over = True
            
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                player.move_down()
            
            if pygame.key.get_pressed()[pygame.K_UP]:
                player.move_up()

            if pygame.key.get_pressed()[pygame.K_LEFT]:
                player.move_left()

            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                player.move_right()
    
        if event.type == pygame.QUIT:
            game_over = True
    
    for bit in snake:
        bit.move()
    
    if(food.x == player.x and food.y == player.y):
        food.generate()
        gameSettings.score+=1
        gameSettings.snake_pieces+=1
        snake.append(SnakeSection(player.x-1, player.y, gameSettings.snake_pieces,True))

    
    pygame.display.update()
    
    time.sleep(mainSettings.REFRESH_RATE)

    


     
