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
    def __init__(self, x, y, color):
        super(Player, self).__init__()
        self.image = pygame.Surface((80, 80))
        self.image.fill(color)
        self.rect=self.image.get_rect(center=(x, y))
        self.jump_count=0
    
    def gravity(self):
        self.rect.centery+=10

        


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Enemy, self).__init__()
        self.image = pygame.Surface((80, 80))
        self.image.fill("grey")
        self.rect=self.image.get_rect(center=(x, y))
        self.deltax=-2
    
    def gravity(self):
        self.rect.centery+=10

    def move(self):
        if self.rect.left <0 or self.rect.right >1000:
            self.deltax*=-1
        self.rect.centerx+=self.deltax


font=pygame.font.Font(None, 100)


plate1=Plate_form(180, 730, 350, 20, 0, "white")
plate2=Plate_form(820, 730, 350, 20, 0, "white")
plate3=Plate_form(500, 550, 250, 20, 100, "white")
plate4=Plate_form(820, 320, 350, 20, 0, "red")
plate5=Plate_form(180, 320, 350, 20, 0, "blue")
plate6=Plate_form(500, 100, 150, 20, 0, "yellow")
player1=Player(100, 600, "red")
player2=Player(900, 600, "blue")
enemy=Enemy(500, 400)
platforms= pygame.sprite.Group()
players= pygame.sprite.Group()
enemies= pygame.sprite.Group()
platforms.add(plate1, plate2, plate3, plate4, plate5, plate6)
players.add(player1, player2)
enemies.add(enemy)
bad_blue=pygame.sprite.Group()
bad_red=pygame.sprite.Group()
bad_blue.add(plate5)
bad_red.add(plate4)
winning_plate=pygame.sprite.Group()
winning_plate.add(plate6)
jump_count_p1=0
jump_count_p2=0
random_1=random.randint(400, 700)
random_2=random.randint(400, 700)
count=0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    keys=pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player1.rect.centerx+=6
    if keys[pygame.K_a]:
        player1.rect.centerx-=6
    if keys[pygame.K_RIGHT]:
        player2.rect.centerx+=6
    if keys[pygame.K_LEFT]:
        player2.rect.centerx-=6


    platforms.draw(screen)
    players.draw(screen)
    enemies.draw(screen)
    for plates in platforms:
        plates.move()
    for enemie in enemies:
        enemie.move()
        if not pygame.sprite.spritecollide(enemie, platforms, False):
            enemie.gravity()
    if not pygame.sprite.spritecollide(player1, platforms, False):
        player1.gravity()
    if not pygame.sprite.spritecollide(player2, platforms, False):
        player2.gravity()
    if pygame.sprite.spritecollide(player1, enemies, False) or player1.rect.bottom>=800 or pygame.sprite.spritecollide(player1, bad_blue, False):
        text_surface=font.render("loss", False, "red")
        text_rect = text_surface.get_rect(center=(screen_width//2, screen_height//2))
        screen.blit(text_surface,text_rect) 
        running=False
    if pygame.sprite.spritecollide(player2, enemies, False) or player1.rect.bottom>=800 or pygame.sprite.spritecollide(player2, bad_red, False):
        text_surface=font.render("loss", False, "red")
        text_rect = text_surface.get_rect(center=(screen_width//2, screen_height//2))
        screen.blit(text_surface,text_rect)
        running=False
    if pygame.sprite.spritecollide(player1, winning_plate, False) and pygame.sprite.spritecollide(player2, winning_plate, False):
        text_surface=font.render("win", False, "green")
        text_rect = text_surface.get_rect(center=(screen_width//2, screen_height//2))
        screen.blit(text_surface,text_rect)
        running=False
    if pygame.sprite.spritecollide(player1, platforms, False) and keys[pygame.K_w] and jump_count_p1<10:
        jump_count_p1+=34
        
    if jump_count_p1>=0:
        jump_count_p1-=1
        player1.rect.centery-=jump_count_p1
    if pygame.sprite.spritecollide(player2, platforms, False) and keys[pygame.K_UP] and jump_count_p2<10:
        jump_count_p2+=34
        
    if jump_count_p2>=0:
        jump_count_p2-=1
        player2.rect.centery-=jump_count_p2
    if count/random_1==1:
        enemies.add(Enemy(40, 50))
        random_1=random.randint(400, 700)
        random_2=random.randint(400, 700)
        print(random_1)
        count=0
    if count/random_2==1:
        enemies.add(Enemy(960, 50))
        random_1=random.randint(400, 700)
        random_2=random.randint(400, 700)
        print(random_2)
        count=0        
    count+=1
    

    clock.tick(60)
    pygame.display.flip()

pygame.time.wait(2000)

pygame.quit()
sys.exit()

# it dosent mader how they look, what maders is how they are as a person - Irmoon 2/11/2025 