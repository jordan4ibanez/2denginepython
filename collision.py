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
		(255,0,0),
		[

			20,#pos  x
			20,#pos  y
			40,#size x
			40,#size y
			0,#inertia
		],
	],
	[ #entity 1
		"rectangle",#shape
		"entity", #physical or fixture
		(0,255,0),
		[

			200,#pos  x
			200,#pos  y
			60,#size x
			60,#size y
			0,#inertia
		],
	],
	[ #entity 2
		"rectangle",#shape
		"entity", #physical or fixture
		(0,0,255),
		[

			400,#pos  x
			400,#pos  y
			30,#size x
			30,#size y
			0,#inertia
		],
	],
]

w = 0
while w < 2000:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:sys.exit()
	screen.fill(white)
	#render entities, if entity does not exist, pass
	for x in range(len(entity_table)):
		if entity_table[x][0] == "rectangle":
			#take raw list data and convert to applicable rendering data
			posx  = entity_table[x][3][0]
			posy  = entity_table[x][3][1]
			sizex = entity_table[x][3][2]
			sizey = entity_table[x][3][3]
			color = entity_table[x][2]
			point1 = (posx - (sizex/2),posy - (sizey/2))
			point2 = (posx + (sizex/2),posy - (sizey/2))
			point3 = (posx + (sizex/2),posy + (sizey/2))
			point4 = (posx - (sizex/2),posy + (sizey/2))
			
			pygame.draw.polygon(screen,color,(point1,point2,point3,point4))

	pygame.display.flip()
	
	#Collision detections
	#for i in range(len(entity_table)):
	
	entity_table[0][3][0],entity_table[0][3][1] = pygame.mouse.get_pos()
	
	for x in range(len(entity_table)):
		for y in range(len(entity_table)):
			if x == y:
				break
			#box 0 (black)
			posax  = entity_table[x][3][0]
			posay  = entity_table[x][3][1]
			sizeax = entity_table[x][3][2]
			sizeay = entity_table[x][3][3]
			pointa1 = (posax - (sizeax/2),posay - (sizeay/2))#topleft
			pointa2 = (posax + (sizeax/2),posay - (sizeay/2))#topright
			pointa3 = (posax + (sizeax/2),posay + (sizeay/2))#bottomright
			pointa4 = (posax - (sizeax/2),posay + (sizeay/2))#bottomleft
			topa    = (pointa1[1]+pointa2[1])/2
			bottoma = (pointa3[1]+pointa4[1])/2
			lefta   = (pointa1[0]+pointa4[0])/2
			righta  = (pointa2[0]+pointa3[0])/2
			

			#box1(red)
			posbx  = entity_table[y][3][0]
			posby  = entity_table[y][3][1]
			sizebx = entity_table[y][3][2]
			sizeby = entity_table[y][3][3]
			pointb1 = (posbx - (sizebx/2),posby - (sizeby/2))
			pointb2 = (posbx + (sizebx/2),posby - (sizeby/2))
			pointb3 = (posbx + (sizebx/2),posby + (sizeby/2))
			pointb4 = (posbx - (sizebx/2),posby + (sizeby/2))
			topb    = (pointb1[1]+pointb2[1])/2
			bottomb = (pointb3[1]+pointb4[1])/2
			leftb   = (pointb1[0]+pointb4[0])/2
			rightb  = (pointb2[0]+pointb3[0])/2	
			

			if topa > bottomb or bottoma < topb or lefta > rightb or righta < leftb:
				pass
			else:
				xdiff = abs(posax-posbx)
				ydiff = abs(posay-posby)
				
				if xdiff >= ydiff:
					if posax >= posbx:
						entity_table[x][3][0] = posbx + ((sizeax/2)+(sizebx/2))
					if posax < posbx:
						entity_table[x][3][0] = posbx - ((sizeax/2)+(sizebx/2))	
				if xdiff < ydiff:	
					if posay >= posby:
						entity_table[x][3][1] = posby + ((sizeay/2)+(sizeby/2))
					if posay < posby:
						entity_table[x][3][1] = posby - ((sizeay/2)+(sizeby/2))	
				
