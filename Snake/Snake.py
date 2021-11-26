import pygame


# Initial configurations
pygame.display.set_caption("Snake.py")
color = (255,255,255)
rectangle = pygame.Rect(5,5,60,60)
screen = pygame.display.set_mode((800,600))
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

square1 = Square();

def draw_at(square,x,y):
    pygame.draw.rect(screen,GREEN,square1.rectangle);

# Main game loop

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if pygame.K_ESCAPE:
                game_over = True
        
        if event.type == pygame.QUIT:
            game_over = True


    draw_at(square1,40,40)
    
    pygame.display.update();

    


     
