import pygame, sys
from pygame import *


class PLAYER:
    def __init__(self,player,x,y):
        self.player = player
        self.rect = pygame.Rect(x,y,120,150)
        self.attacking = 0
        self.health = 100
        self.face = False
        self.attacking = False

    def draw(self,player_image,attack_image):
       img = pygame.transform.flip(player_image, self.face, False)
       img_attack = pygame.transform.flip(attack_image, self.face, False)

       if self.attacking > 0:
        screen.blit(img_attack,self.rect)
       else:
        screen.blit(img,self.rect)
           


    def attack(self,target):
        self.attacking = 30
        attack_rect = pygame.Rect(self.rect.centerx - (1.5 * self.rect.width * self.face),self.rect.y,self.rect.width *1.5,self.rect.height)
        if attack_rect.colliderect(target.rect):
            target.health -= 5
            
        #pygame.draw.rect(surface,'green',attack_rect)


    def update(self,target):
        gravity = 0

        #player1 
        if self.player == 1:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d] and self.rect.right < 1190:
                self.rect.centerx += 20
            if keys[pygame.K_a] and self.rect.left > 30:
                self.rect.centerx -= 20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.rect.centery > 300 :
                    gravity = -60
            if self.attacking == 0:    
                if keys[pygame.K_LSHIFT]:
                    self.attack(target)        
            #facing
            if target.rect.centerx > self.rect.centerx: self.face = False
            else: self.face = True
            
            #attack cooldown
            if self.attacking > 0:
                self.attacking -= 1
            #gravity
            gravity += 15
            self.rect.centery += gravity
            if self.rect.centery >= 495 : self.rect.centery = 495
        

       #player2
        if self.player == 2:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT] and self.rect.right < 1190:
                self.rect.centerx += 20
            if keys[pygame.K_LEFT] and self.rect.left > 10:
                self.rect.centerx -= 20
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.rect.centery > 300 :
                    gravity = -60
            
            if self.attacking == False:    
                if keys[pygame.K_RSHIFT]:
                    self.attack(target)
            #facing
            if target.rect.centerx > self.rect.centerx: self.face = False
            else: self.face = True

            #attack cooldown
            if self.attacking > 0:
                self.attacking -= 1
            
            #gravity
            gravity += 15
            self.rect.centery += gravity
            if self.rect.centery >= 495 : self.rect.centery = 495


pygame.init()
screen = pygame.display.set_mode((1200, 600))
ground = pygame.image.load("graphics/ground.jpeg").convert()
sky = pygame.image.load("graphics/sky.png").convert()
clock = pygame.time.Clock()
screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update, 150)

player_1_graphics = pygame.image.load("graphics/player1.png").convert_alpha()
player_2_graphics = pygame.image.load("graphics/player2.png").convert_alpha()
player_1_attack = pygame.image.load("graphics/player_1_knife.png").convert_alpha()
player_2_attack = pygame.image.load("graphics/player_2_knife.png").convert_alpha()
orb_graphics = pygame.image.load("graphics/rasengan.png").convert_alpha()

player_1 = PLAYER(1,100,420)
player_2 = PLAYER(2,1000,420)



def draw_health(health,x,y):
    loss = health/100
    pygame.draw.rect(sky,'white',(x-2,y-2,504,34))
    pygame.draw.rect(sky,'red',(x,y,500,30))
    pygame.draw.rect(sky,'green',(x,y,500 * loss,30))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    gravity = 0

    screen.blit(sky,(0,0))
    screen.blit(ground, (0, 550))

    draw_health(player_1.health,20,20)
    draw_health(player_2.health,680,20)


    player_1.update(player_2)
    player_2.update(player_1)

    player_1.draw(player_1_graphics,player_1_attack)
    player_2.draw(player_2_graphics,player_2_attack)
   
   
    
    
    
    pygame.display.update()
    clock.tick(60)
