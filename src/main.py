import pygame, sys, random
from pygame.math import Vector2
from pygame import *



class PLAYER_1:
	def __init__(self):
		self.player_1_x = 5
		self.player_1_y = 21
		self.player_pos = (self.player_1_x,self.player_1_y)
	def draw_player_1(self):
		player_1_rect = pygame.Rect(int(self.player_1_x*cell_size),int(self.player_1_y*cell_size),120,150)
		screen.blit(player_1_graphics,player_1_rect)
		# pygame.draw.rect(screen,"red",player_1_rect)

         

	

class PLAYER_2:
	def __init__(self):
		self.player_2_x = 50
		self.player_2_y = 21
	def draw_player_2(self):
		player_2_rect = pygame.Rect(int(self.player_2_x*cell_size),int(self.player_2_y*cell_size),120,150)
		screen.blit(player_2_graphics,player_2_rect)
		# pygame.draw.rect(screen,"blue",player_2_rect)
		
	



class ATTACK:
	def __init__(self):
		self.player_1 = PLAYER_1()
		self.orb_x = self.player_1.player_1_x
		self.orb_y = self.player_1.player_1_y
	def attack_1(self):
		orb = pygame.Rect((self.orb_x+(self.orb_x/2)),(self.orb_y+(self.orb_y/2)),20,20)
		pygame.draw.rect(screen,"yellow",orb)
		# while self.orb_y<99:
		# 	self.orb_x += 4
			
		


class MAIN():
	def __init__(self):
		self.player_1 = PLAYER_1()
		self.player_2 = PLAYER_2()
		self.attack = ATTACK()
	
	def update(self):
		pass


pygame.init()
cell_size = 20
screen = pygame.display.set_mode((1200,600))
ground = pygame.image.load('graphics/ground.jpeg').convert()
sky = pygame.image.load('graphics/sky.png').convert()
clock = pygame.time.Clock()
screen_update = pygame.USEREVENT
pygame.time.set_timer(screen_update,150)

player_1_graphics = pygame.image.load('graphics/player1.png').convert_alpha()
player_2_graphics = pygame.image.load('graphics/player2.png').convert_alpha()

player_1_gravity = 0
player_2_gravity = 0

main = MAIN()
player_1 = PLAYER_1()
player_2 = PLAYER_2()
attack = ATTACK()			



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == screen_update:
			main.update()
		
		keys = pygame.key.get_pressed()	
		if keys[pygame.K_RIGHT] and player_1.player_1_x < 56 :
				player_1.player_1_x += 2
		if keys[pygame.K_LEFT] and player_1.player_1_x > 2 :
				player_1.player_1_x -= 2
		if keys[pygame.K_d] and player_2.player_2_x < 56:
				player_2.player_2_x += 2
		if keys[pygame.K_a] and player_2.player_2_x > 1:
				player_2.player_2_x -= 2	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and player_1.player_1_y > 15 :
				player_1_gravity = -4
			if event.key == pygame.K_w and player_2.player_2_y > 15:
				player_2_gravity = -4
			if event.key == pygame.K_RCTRL:
				attack.attack_1()
 	

	player_1_gravity += 0.5
	player_2_gravity += 0.5
	player_1.player_1_y += player_1_gravity
	player_2.player_2_y += player_2_gravity
	if player_1.player_1_y >= 21 : player_1.player_1_y = 21
	if player_2.player_2_y >= 21 : player_2.player_2_y = 21
	screen.blit(sky,(0,0))
	screen.blit(ground,(0,550))			
	player_1.draw_player_1()
	player_2.draw_player_2()
	# attack.attack_1()			
	pygame.display.update()
	clock.tick(60)




		    			
	
	