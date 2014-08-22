#this is 3d testing and is completely experimental in case I decide to merge this little engine into a 3d engine for a racing game which temporarily uses 2d physics
#then merged into 3d maybe
#maybe even a rollercoaster tycoon clone
#3d pong?
#doom clone?
#probably a racing game

import pygame, sys, os, time, pygame.gfxdraw

screensize = width,height = 1000,800
screen = pygame.display.set_mode(screensize)
clock = pygame.time.Clock()
pygame.init()
font = pygame.font.Font("font/Kirvy-Regular.otf", 10)
fontbig = pygame.font.Font("font/Kirvy-Regular.otf", 30)
black = 0,0,0
white = 255,255,255
red   = 255,0,0
blue  = 0,0,255
pygame.init()

while 1:
	screen.fill((255, 255, 255))
	clock.tick()

	for x in range(50):
		for y in range(50):
			#pygame.gfxdraw.aacircle(screen, 50, 50, 30, col)
			pygame.gfxdraw.filled_circle(screen, 50, 80, 30, black)
				
	fps = round(clock.get_fps())
	fps_text = fontbig.render(str(fps), 1, black)
	screen.blit(fps_text, (10,10))
	
	pygame.display.flip()
