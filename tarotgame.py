import pygame

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
icon = pygame.image.load("res/pygame_icon.png")

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Tarot Game")
pygame.display.set_icon(icon)

# Game loop
run = True
while run:

    screen.fill((128, 0 ,32))
    
    #event handler windows quit clicked
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run =False

    pygame.display.update()

pygame.quit()