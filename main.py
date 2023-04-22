import pygame,sys,random
from pygame.math import Vector2



class PLAYER_1:
	def __init__(self):
		pass
	def draw_player_1(self):
	
		player_1_rect = pygame.Rect(int(player_1_x*cell_size),int(player_1_y*cell_size),60,150)
		pygame.draw.rect(screen,"red",player_1_rect)




class PLAYER_2:
	def __init__(self):
		pass
	def draw_player_2(self):
	
		player_2_rect = pygame.Rect(int(player_2_x*cell_size),int(player_2_y*cell_size),60,150)
		pygame.draw.rect(screen,"blue",player_2_rect)






pygame.init()
cell_size = 20
screen = pygame.display.set_mode((1200,600))
ground = pygame.Surface((1200,125))
ground.fill(pygame.Color("green"))
clock = pygame.time.Clock()
player_1 = PLAYER_1()
player_2 = PLAYER_2()


player_1_x = 5
player_1_y = 20

player_2_x = 50
player_2_y = 20



while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT and player_1_x < 56 :
				player_1_x += 3
			if event.key == pygame.K_LEFT and player_1_x > 2 :
				player_1_x -= 3
			if event.key == pygame.K_d and player_2_x < 56:
				player_2_x += 3
			if event.key == pygame.K_a and player_2_x > 1:
				player_2_x -= 3	
	
	
	screen.fill(("white"))
	screen.blit(ground,(0,550))
	player_1.draw_player_1()
	player_2.draw_player_2()
	pygame.display.update()
	clock.tick(60)