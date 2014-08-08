import pygame,sys,os,time

screensize = width,height = 1000,800
screen = pygame.display.set_mode(screensize)
pygame.init()

black = 0,0,0
white = 255,255,255
red = 255,0,0
#rectangular collision boxes, symetrical to allow quickndirty detection, with oft size/pos modifications
entity_table = [
	[ #entity 0
		"rectangle",#shape
		"entity", #physical or fixture
		[

			20,#pos  x
			20,#pos  y
			40,#size x
			40,#size y
		],
	],
	[ #entity 1
		"rectangle",#shape
		"entity", #physical or fixture
		[

			100,#pos  x
			50,#pos  y
			40,#size x
			40,#size y
		],
	],
]
"""
[0,0], #top left
[40,0], #top right
[40,40], #bottom right
[0,40], #bottom left
"""
w = 0
while w < 2000:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:sys.exit()
	screen.fill(white)
	#render entities, if entity does not exist, pass
	for x in range(len(entity_table)):
		if entity_table[x][0] == "rectangle":
			#take raw list data and convert to applicable rendering data
			posx  = entity_table[x][2][0]
			posy  = entity_table[x][2][1]
			sizex = entity_table[x][2][2]
			sizey = entity_table[x][2][3]
			point1 = (posx - (sizex/2),posy - (sizey/2))
			point2 = (posx + (sizex/2),posy - (sizey/2))
			point3 = (posx + (sizex/2),posy + (sizey/2))
			point4 = (posx - (sizex/2),posy + (sizey/2))
			if x == 0:
				pygame.draw.polygon(screen,black,(point1,point2,point3,point4))
			if x == 1:
				pygame.draw.polygon(screen,red,(point1,point2,point3,point4))

	pygame.display.flip()
	
	#Collision detections
	#for i in range(len(entity_table)):
	
	#move for testing
	entity_table[0][2][0],entity_table[0][2][1] = pygame.mouse.get_pos()
	
	entity_table[1][2][0] = posbx  = entity_table[1][2][0] + 0.1
	entity_table[1][2][1] = posbx  = entity_table[1][2][1] + 0.1
	
	#box 0 (black)
	posax  = entity_table[0][2][0]
	posay  = entity_table[0][2][1]
	sizeax = entity_table[0][2][2]
	sizeay = entity_table[0][2][3]
	pointa1 = (posax - (sizeax/2),posay - (sizeay/2))#topleft
	pointa2 = (posax + (sizeax/2),posay - (sizeay/2))#topright
	pointa3 = (posax + (sizeax/2),posay + (sizeay/2))#bottomright
	pointa4 = (posax - (sizeax/2),posay + (sizeay/2))#bottomleft

	#box1(red)
	posbx  = entity_table[1][2][0]
	posby  = entity_table[1][2][1]
	sizebx = entity_table[1][2][2]
	sizeby = entity_table[1][2][3]
	pointb1 = (posbx - (sizebx/2),posby - (sizeby/2))
	pointb2 = (posbx + (sizebx/2),posby - (sizeby/2))
	pointb3 = (posbx + (sizebx/2),posby + (sizeby/2))
	pointb4 = (posbx - (sizebx/2),posby + (sizeby/2))
	
	#test top left of ent a, with bottom right of ent b.
	#make sure ent a bottom right not within ent b.
	if pointa1[0] <= pointb3[0] and pointa1[1] <= pointb3[1]:
		if pointa3[0] >= pointb3[0] and pointa3[1] >= pointb3[1]:
			#test for which corner to set ent a at.
			#have this balance out detection based on size of ents.
			if abs(pointa1[0]-pointb3[0]) < abs(pointa1[1]-pointb3[1]):
				entity_table[0][2][0] = posbx + ((sizeax/2)+(sizebx/2))
			#elif abs(pointa1[0]-pointb3[0]) > abs(pointa1[1]-pointb3[1]):
			else:
				entity_table[0][2][1] = posby + ((sizeay/2)+(sizeby/2))
			
	#test top right of a with bottom left of b
	if pointa2[0] >= pointb4[0] and pointa2[1] <= pointb4[1]:
		if pointa4[0] <= pointb4[0] and pointa4[1] >= pointb4[1]:
			if abs(pointa2[0]-pointb4[0]) < abs(pointa2[1]-pointb4[1]):
				entity_table[0][2][0] = posbx - ((sizeax/2)+(sizebx/2))
			#elif abs(pointa2[0]-pointb4[0]) > abs(pointa2[1]-pointb4[1]):
			else:
				entity_table[0][2][1] = posby + ((sizeay/2)+(sizeby/2))

	#test bottom right of a with top left of b
	if pointa3[0] >= pointb1[0] and pointa3[1] >= pointb1[1]:
		if pointa1[0] <= pointb1[0] and pointa1[1] <= pointb1[1]:
			if abs(pointa3[0]-pointb1[0]) < abs(pointa3[1]-pointb1[1]):
				entity_table[0][2][0] = posbx - ((sizeax/2)+(sizebx/2))
			#elif abs(pointa3[0]-pointb1[0]) > abs(pointa3[1]-pointb1[1]):
			else:
				entity_table[0][2][1] = posby - ((sizeay/2)+(sizeby/2))
				
	#test bottom left with top right
	if pointa4[0] <= pointb2[0] and pointa4[1] >= pointb2[1]:
		if pointa2[0] >= pointb2[0] and pointa2[1] <= pointb2[1]:
			if abs(pointa4[0]-pointb2[0]) < abs(pointa4[1]-pointb2[1]):
				entity_table[0][2][0] = posbx + ((sizeax/2)+(sizebx/2))
			#elif abs(pointa4[0]-pointb2[0]) > abs(pointa4[1]-pointb2[1]):
			else:
				entity_table[0][2][1] = posby - ((sizeay/2)+(sizeby/2))
