import pygame
import sys
import random
import math
pygame.init()

screen_width = 1000
screen_height = 760
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Tutorial")
clock = pygame.time.Clock()
screen.fill("white")





class Plate_form(pygame.sprite.Sprite):
    def __init__(self, x, y, sizex, sizey):
        super(Plate_form, self).__init__()
        self.image = pygame.Surface((sizex, sizey))
        self.image.fill("black")
        self.rect=self.image.get_rect(center=(x, y))

plate=Plate_form(100, 100, 100, 100)
platforms= pygame.sprite.Group()
platforms.add(plate)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    platforms.draw(screen)

    clock.tick(60)
    pygame.display.flip()


pygame.quit()
sys.exit()
