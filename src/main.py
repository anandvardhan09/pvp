import pygame,sys,random
from pygame.math import Vector2

class PLAYER_1:
	def __init__(self):
		pass
	
	def draw_player_1(self):
		player_1_rect = pygame.Rect(5*cell_size,20*cell_size,60,150)
		pygame.draw.rect(screen,"red",player_1_rect)

pygame.init()
cell_size = 20
screen = pygame.display.set_mode((1200,600))

player_1 = PLAYER_1()

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
			
	
	screen.fill(("white"))
	player_1.draw_player_1()
	pygame.display.update()			
