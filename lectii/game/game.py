import pygame
import os
#dimensiunile ferestri in care vom juca jocul
width = 900
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Joc spatial")

#fps - frame per second
fps = 60
spaceship_width = 80
spaceship_height = 60

yellow_spaceship_image = pygame.image.load(os.path.join('lectii/game/Assets', 'spaceship_yellow.png'))
red_spaceship_image = pygame.image.load(os.path.join('lectii/game/Assets', 'spaceship_red.png'))

red_spaceship = pygame.transform.scale(red_spaceship_image, (spaceship_width, spaceship_height))
yellow_spaceship = pygame.transform.scale(yellow_spaceship_image, (spaceship_width, spaceship_height))

def drawWindow(red, yellow):
    # r g b
    window.fill((255, 255, 255))
    window.blit(yellow_spaceship, (yellow.x, yellow.y))
    window.blit(red_spaceship, (red.x, red.y))
    pygame.display.update()

def main():
    yellow = pygame.Rect(700, 300, spaceship_width, spaceship_height)
    red = pygame.Rect(100, 300, spaceship_width, spaceship_height)
    #event handleing
    #controlam navele 
    #update
    clock = pygame.time.Clock()
    gameOver = False
    while not gameOver:
        clock.tick(fps)

        for event in pygame.event.get(): #lista de evenimente
            if event.type == pygame.QUIT:
                gameOver = True
        #even based 
        drawWindow(red, yellow)

main()