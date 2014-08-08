import pygame,sys,os,time

screensize = width,height = 1000,800
screen = pygame.display.set_mode(screensize)
pygame.init()

black = 0,0,0
white = 255,255,255

entity_table = {
	"ent0":
	{
		"type":  "rectangle",
		"vertices":
		(
			(10,10), #top left
			(40,10), #top right
			(40,40), #bottom right
			(10,40), #bottom left
		),
	},
}

w = 0
while w < 2000:
	screen.fill(white)
	#render entities, if entity does not exist, pass
	for x in range(1):
		for y in range(2):
			if entity_table["ent"+str(x)]["type"] == "rectangle":
				pygame.draw.polygon(screen,black,entity_table["ent"+str(x)]["vertices"])
	w = w + 1
	pygame.display.flip()
	
