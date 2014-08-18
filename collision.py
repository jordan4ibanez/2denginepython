import pygame,sys,os,time

screensize = width,height = 1000,800
screen = pygame.display.set_mode(screensize)
pygame.init()
font = pygame.font.Font("font/Kirvy-Regular.otf", 10)

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

			50,#pos  x
			400,#pos  y
			40,#size x
			40,#size y
			[0,0],#inertia
			100,#bounce %
		],
	],
	[ #entity 1
		"rectangle",#shape
		"entity", #physical or fixture
		(0,255,0),
		[

			700,#pos  x
			400,#pos  y
			60,#size x
			60,#size y
			[0,0],#inertia
			100,#bounce %
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
			[0,0],#inertia
			100,#bounce %
		],
	],
	[ #entity 3
		"rectangle",#shape
		"entity", #physical or fixture
		(0,0,255),
		[
			500,#pos  x
			400,#pos  y
			30,#size x
			30,#size y
			[0,0],#inertia
			100,#bounce %
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
			text = font.render(str(x), 1, (10, 10, 10))
			screen.blit(text, (posx,posy))
			
	pygame.display.flip()
	
	
	#debug for player entity
	#clean this up and make this it's own function eventually
	
	key = pygame.key.get_pressed()
	#X
	if key[pygame.K_RIGHT]:
		entity_table[1][3][4][0] = entity_table[1][3][4][0] + 0.1
	elif key[pygame.K_LEFT]:
		entity_table[1][3][4][0] = entity_table[1][3][4][0] - 0.1
	#Y	
	if key[pygame.K_UP]:
		entity_table[1][3][4][1] = entity_table[1][3][4][1] - 0.1
	elif key[pygame.K_DOWN]:
		entity_table[1][3][4][1] = entity_table[1][3][4][1] + 0.1
	
	#momentum	
	for x in range(len(entity_table)):
		entity_table[x][3][0] = entity_table[x][3][0] + entity_table[x][3][4][0]
		entity_table[x][3][1] = entity_table[x][3][1] + entity_table[x][3][4][1]
		#slow down for test air resistance x
		if entity_table[x][3][4][0] > 0:
			entity_table[x][3][4][0] = entity_table[x][3][4][0] - 0.05
		elif entity_table[x][3][4][0] < 0:
			entity_table[x][3][4][0] = entity_table[x][3][4][0] + 0.05
		#correct for floating point error
		if entity_table[x][3][4][0] < 0.05 and entity_table[x][3][4][0] > -0.05:
			entity_table[x][3][4][0] = 0
		#slow down for test air resistance y
		if entity_table[x][3][4][1] > 0:
			entity_table[x][3][4][1] = entity_table[x][3][4][1] - 0.05
		elif entity_table[x][3][4][1] < 0:
			entity_table[x][3][4][1] = entity_table[x][3][4][1] + 0.05
		#correct for floating point error
		if entity_table[x][3][4][1] < 0.05 and entity_table[x][3][4][1] > -0.05:
			entity_table[x][3][4][1] = 0 
	
	#Collision detections
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
			inertxa = entity_table[x][3][4][0]
			inertya = entity_table[x][3][4][1] 
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
			inertxb = entity_table[y][3][4][0]
			inertyb = entity_table[y][3][4][1]
			
			#if outside range pass, if in, do bounding box sorting
			if topa > bottomb or bottoma < topb or lefta > rightb or righta < leftb:
				pass
			else:

				xdiff = abs(posax-posbx)
				ydiff = abs(posay-posby)
				if xdiff >= ydiff:
					#compare inertia of a to b
					if abs(inertxa) < abs(inertxb):
						if posax >= posbx:
							entity_table[x][3][0] = posbx + ((sizeax/2)+(sizebx/2)) + 1
							#transfer inertia
							entity_table[x][3][4][0] = entity_table[y][3][4][0]
						if posax < posbx:
							entity_table[x][3][0] = posbx - ((sizeax/2)+(sizebx/2)) - 1
							entity_table[x][3][4][0] = entity_table[y][3][4][0]
					if abs(inertxa) > abs(inertxb):
						if posax <= posbx:
							entity_table[y][3][0] = posax + ((sizeax/2)+(sizebx/2)) + 1
							entity_table[y][3][4][0] = entity_table[x][3][4][0]
						if posax > posbx:
							entity_table[y][3][0] = posax - ((sizeax/2)+(sizebx/2)) - 1
							entity_table[y][3][4][0] = entity_table[x][3][4][0]
					#do equal inertia for kicks
					if abs(inertxa) == abs(inertxb):
						if posax <= posbx:
							entity_table[y][3][0] = posax + ((sizeax/2)+(sizebx/2)) + 1
							entity_table[y][3][4][0] = 0
							entity_table[x][3][4][0] = 0							
						if posax > posbx:
							entity_table[y][3][0] = posax - ((sizeax/2)+(sizebx/2)) - 1
							entity_table[y][3][4][0] = 0
							entity_table[x][3][4][0] = 0
				if xdiff <= ydiff:
					#compare inertia of a to b
					if abs(inertya) < abs(inertyb):
						if posay >= posby:
							entity_table[x][3][1] = posby + ((sizeay/2)+(sizeby/2)) + 2
							#transfer inertia
							entity_table[x][3][4][1] = entity_table[y][3][4][1]
						if posay < posby:
							entity_table[x][3][1] = posby - ((sizeay/2)+(sizeby/2)) - 2
							entity_table[x][3][4][1] = entity_table[y][3][4][1]
					if abs(inertya) > abs(inertyb):
						if posay <= posby:
							entity_table[y][3][1] = posay + ((sizeay/2)+(sizeby/2)) + 2
							entity_table[y][3][4][1] = entity_table[x][3][4][1]
						if posay > posby:
							entity_table[y][3][1] = posay - ((sizeay/2)+(sizeby/2)) - 2
							entity_table[y][3][4][1] = entity_table[x][3][4][1]
					#do equal inertia for kicks
					if abs(inertya) == abs(inertyb):
						if posay <= posby:
							entity_table[y][3][1] = posay + ((sizeay/2)+(sizeby/2)) + 2
							entity_table[y][3][4][1] = 0
							entity_table[x][3][4][1] = 0							
						if posay > posby:
							entity_table[y][3][1] = posay - ((sizeay/2)+(sizeby/2)) - 2
							entity_table[y][3][4][1] = 0
							entity_table[x][3][4][1] = 0
