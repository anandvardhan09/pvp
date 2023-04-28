import pygame, sys, random
from pygame.math import Vector2
from pygame import *


class PLAYER:
    def __init__(self,x,y):
      
        self.rect = pygame.Rect(x,y,120,150)

    def draw(self,player_image):
       screen.blit(player_image,self.rect)

    # def attack( ):

        

# class PLAYER_2:
#     def __init__(self):
#         self.player_2_x = 1000
#         self.player_2_y = 420

#     def draw_player_2(self):
#         player_2_rect = pygame.Rect(int(self.player_2_x), int(self.player_2_y), 120, 150)
#         screen.blit(player_2_graphics, player_2_rect)
#         # pygame.draw.rect(screen,"blue",player_2_rect)


# class ORB_ATTACK:
#     def __init__(self,x,y):
#         self.rect = pygame.Rect(x,y,40,40)
#         # self.player_1 = PLAYER()
#         # self.orb_x_1 = self.player_1.player_1_x + 120
#         # self.orb_y_1 = self.player_1.player_1_y + 75

#     def draw(self,orb_image):
#         screen.blit(orb_image, self.rect)


# class ATTACK_2:
#     def __init__(self):
#         self.player_2 = PLAYER()
#         self.orb_x_2 = self.player_2.player_2_x - 120
#         self.orb_y_2 = self.player_2.player_2_y + 75

#     def attack(self):
#         orbplayer2 = pygame.Rect(self.orb_x_2, self.orb_y_2, 40, 40)
#         screen.blit(orb_graphics, orbplayer2)
        # pygame.draw.rect(screen,"yellow",orb)


# class MAIN:
#     def __init__(self):
#         self.player_1 = PLAYER(100,420)
#         self.player_2 = PLAYER(100,420)
#         # self.attack1 = ATTACK_1()
#         # self.attack2 = ATTACK_2()

#     def update(self):
#         pass


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

# player_1_gravity = 0
# player_2_gravity = 0

# main = MAIN()
player_1 = PLAYER(100,420)
player_2 = PLAYER(1000,420)
# attack1 = ATTACK_1()
# # attack2 = ATTACK_2()
# orb_attack_p1 = False
# orb_attack_p2 = False
# player_attack_p1 = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # if event.type == screen_update:
        #     main.update()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and player_1.rect.right < 1120:
            player_1.rect.centerx += 35
        if keys[pygame.K_a] and player_1.rect.left > 40:
            player_1.rect.centerx -= 35
        if keys[pygame.K_RIGHT] and player_2.rect.right < 1120:
            player_2.rect.centerx += 35
        if keys[pygame.K_LEFT] and player_2.rect.left > 10:
            player_2.rect.centerx -= 35

        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_w and player_1.player_1_y > 300:
        #         player_1_gravity = -30
        #     if event.key == pygame.K_UP and player_2.player_2_y > 300:
        #         player_2_gravity = -30
        #     if event.key == pygame.K_LCTRL:
        #         orb_attack_p1 = True
        #     if event.key == pygame.K_RCTRL:
        #         orb_attack_p2 = True
        #     if event.key == pygame.K_LSHIFT:
        #         player_attack_p1 == True

    # player_1_gravity += 2
    # player_2_gravity += 2
    # player_1.y += player_1_gravity
    # player_2.y += player_2_gravity
    # if player_1.y >= 420:
    #     player_1.y = 420
    # if player_2.y >= 420:
    #     player_2.y = 420

    # screen.blit(sky,(0,0))
    # screen.blit(ground, (0, 550))
    player_1.draw(player_1_graphics)
    player_2.draw(player_2_graphics)
    # if orb_attack_p1 == True:
    #     attack1.attack()
    #     attack1.orb_x_1 += 8
    #     if attack1.orb_x_1 > 1200:
    #         orb_attack_p1 = False
    #         attack1.orb_x_1 = player_1.player_1_x + 120

    # if orb_attack_p2 == True:
    #     attack2.attack()
    #     attack2.orb_x_2 -= 8
    #     if attack2.orb_x_2 < 20:
    #         orb_attack_p2 = False
    #         attack2.orb_x_2 = player_2.player_2_x - 120
    pygame.display.update()
    clock.tick(60)
