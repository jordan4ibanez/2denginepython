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

test = 0
while 1:
	#this is a test of gfxdraw vs normal blit speed
	test = test + 1
	if test > 1000:
		test = 0
	clock.tick()
	col = (255, 0, 0)
	screen.fill((255, 255, 255))
	#begin testing
	tester = fontbig.render("Let's draw 50 circles each frame using", 1, black)
	screen.blit(tester, (10,10))
	if test > 500:
		tester = fontbig.render("gfx", 1, red)
		screen.blit(tester, (565,10))
		for x in range(50):
			for y in range(50):
				#pygame.gfxdraw.aacircle(screen, 50, 50, 30, col)
				pygame.gfxdraw.filled_circle(screen, 50, 80, 30, col)
	if test < 500:
		tester = fontbig.render("draw", 1, blue)
		screen.blit(tester, (565,10))
		for x in range(50):
			for y in range(50):
				pygame.draw.circle(screen, red, (50,80), 30)
	#sarcasm
	tester = fontbig.render("<-50 Circles", 1, black)
	screen.blit(tester, (105,60))				
	#print fps
	fps = round(clock.get_fps())
	fps_text = fontbig.render(str(fps), 1, black)
	screen.blit(fps_text, (640,10))
	#end testing
	pygame.display.flip()
