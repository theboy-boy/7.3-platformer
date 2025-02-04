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
screen.fill("black")





class Plate_form(pygame.sprite.Sprite):
    def __init__(self, x, y, sizex, sizey, vert_move, color):
        super(Plate_form, self).__init__()
        self.vert_move=vert_move
        self.count, self.swap=0, False
        self.image = pygame.Surface((sizex, sizey))
        self.image.fill(color)
        self.rect=self.image.get_rect(center=(x, y))
    def move(self):
        total=self.vert_move
        if total==0:
            return
        if self.swap==False:
            self.rect.centerx+=1
            self.count+=1
        if self.swap==True:
            self.rect.centerx-=1
            self.count-=1
        if self.count<=-total:
            self.swap=False
        if self.count>=total:
            self.swap=True




class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Player, self).__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill("red")
        self.rect=self.image.get_rect(center=(x, y))
    
    def gravity(self):
        self.rect.centery+=10
        


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Enemy, self).__init__()
        self.image = pygame.Surface((100, 100))
        self.image.fill("blue")
        self.rect=self.image.get_rect(center=(x, y))
        self.deltax=-2
    
    def gravity(self):
        self.rect.centery+=10

    def move(self):
        if self.rect.left <0 or self.rect.right >1000:
            self.deltax*=-1
        self.rect.centerx+=self.deltax

plate1=Plate_form(180, 730, 350, 20, 0, "white")
plate2=Plate_form(820, 730, 350, 20, 0, "white")
plate3=Plate_form(500, 550, 250, 20, 100, "white")
player1=Player(100, 100)
enemy=Enemy(500, 400)
platforms= pygame.sprite.Group()
players= pygame.sprite.Group()
enemies= pygame.sprite.Group()
platforms.add(plate1, plate2, plate3)
players.add(player1)
enemies.add(enemy)
jump_count=0


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    keys=pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player1.rect.centerx+=4
    if keys[pygame.K_a]:
        player1.rect.centerx-=4

    platforms.draw(screen)
    players.draw(screen)
    enemies.draw(screen)
    for plates in platforms:
        plates.move()
    for enemie in enemies:
        enemie.move()
    if not pygame.sprite.spritecollide(player1, platforms, False):
        player1.gravity()

    if not pygame.sprite.spritecollide(enemy, platforms, False):
        enemy.gravity()
    if pygame.sprite.spritecollide(player1, enemies, False) or player1.rect.bottom>=800:
        pygame.time.wait(2000)
        running=False
    if pygame.sprite.spritecollide(player1, platforms, False) and keys[pygame.K_w]:
        jump_count+=34
    if jump_count>=0:
        jump_count-=1
        player1.rect.centery-=jump_count




    clock.tick(60)
    pygame.display.flip()


pygame.quit()
sys.exit()
