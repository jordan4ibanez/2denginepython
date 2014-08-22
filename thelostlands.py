import pygame,sys,os,time, pygame.gfxdraw

screensize = width,height = 1000,800
screen = pygame.display.set_mode(screensize)
pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font("font/Kirvy-Regular.otf", 10)
fontbig = pygame.font.Font("font/Kirvy-Regular.otf", 30)
gravity_strength = 0.2
max_velocity = 12
jump_strength = 5
black = 0,0,0
white = 255,255,255
red = 255,0,0
on_ground = False
framerate = 60

#do average framerate counter, add in a table of 60fps, then add them up and divide by 60
#blocks will be 40 big
#remember to go through terrain y to x when doing terrain[y][x]
#scale the map up and down to demonstrate the scalability of the map

entity_table = [
	#this is the player
	[ #entity 0
		"rectangle",#shape
		"entity", #physical or fixture
		(255,0,0),
		[

			50,#pos  x
			50,#pos  y
			10,#size x
			30,#size y
			[0,0],#inertia
			100,#bounce %
		],
	],
]
#chunk table
block_table = [
	[0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0],
	[1,0,0,0,0,0,0,1,0,0],
	[1,0,0,0,0,0,0,1,0,0],
	[1,0,0,0,0,0,0,0,0,0],
	[1,0,0,0,1,0,0,0,1,0],
	[1,0,1,0,1,0,0,0,1,0],
	[1,0,0,0,0,0,0,0,1,0],
	[1,0,1,1,1,1,1,1,1,1],
	[1,1,1,1,1,1,1,1,1,1],
]
#block ids
block_id = []

class control:
	def __init__(self, key):
		clock.tick(framerate)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:sys.exit()
		if key[pygame.K_ESCAPE]:
			sys.exit()
		#movement (inertia)
		self.x    = entity_table[0][3][4][0]
		self.y    = entity_table[0][3][4][1]
		self.move = False
		if key[pygame.K_RIGHT]:
			self.x = self.x + 0.2
			self.move = True
		if key[pygame.K_LEFT]:
			self.x = self.x - 0.2
			self.move = True
		if key[pygame.K_UP]:
			entity_table[0][3][4][1] = -jump_strength
			#self.move = True
		#if key[pygame.K_DOWN]:
		#	self.y = self.y + 0.1
		#	self.move = True
		if self.move == False:
			return
		entity_table[0][3][4][0] = self.x
		entity_table[0][3][4][1] = self.y

class render:
	def __init__(self,key):
		clock.tick()
		screen.fill(white)
		#render entities
		for x in range(len(entity_table)):
			if entity_table[x][0] == "rectangle":
				#take raw list data and convert to applicable rendering data
				posx   = entity_table[x][3][0]
				posy   = entity_table[x][3][1]
				sizex  = entity_table[x][3][2]
				sizey  = entity_table[x][3][3]
				color  = entity_table[x][2]
				point1 = (posx - (sizex/2),posy - (sizey/2))
				point2 = (posx + (sizex/2),posy - (sizey/2))
				point3 = (posx + (sizex/2),posy + (sizey/2))
				point4 = (posx - (sizex/2),posy + (sizey/2))
				pygame.draw.polygon(screen,color,(point1,point2,point3,point4))
				#pygame.gfxdraw.polygon(screen, (point1,point2,point3,point4), color)
				entity_box = font.render(str(x), 1, (10, 10, 10))
				screen.blit(entity_box, (posx,posy))
				fps = round(clock.get_fps())
				fps_text = fontbig.render(str(fps), 1, black)
				screen.blit(fps_text, (10,10))
				#debug info			
				text = fontbig.render("ent_"+str(0)+" posx:"+str(posx)+" posy:"+str(posy), 1, (10, 10, 10))
				screen.blit(text, (60,0))
				if key[pygame.K_RIGHT]:
					text = fontbig.render("Right:True", 1, (10, 10, 10))
					screen.blit(text, (600,0))
				else:
					text = fontbig.render("Right:False", 1, (10, 10, 10))
					screen.blit(text, (600,0))
				if key[pygame.K_LEFT]:
					text = fontbig.render("Left:True", 1, (10, 10, 10))
					screen.blit(text, (600,40))
				else:
					text = fontbig.render("Left:False", 1, (10, 10, 10))
					screen.blit(text, (600,40))
				if key[pygame.K_UP]:
					text = fontbig.render("Up:True", 1, (10, 10, 10))
					screen.blit(text, (600,80))
				else:
					text = fontbig.render("Up:False", 1, (10, 10, 10))
					screen.blit(text, (600,80))
				if key[pygame.K_DOWN]:
					text = fontbig.render("Down:True", 1, (10, 10, 10))
					screen.blit(text, (600,120))
				else:
					text = fontbig.render("Down:False", 1, (10, 10, 10))
					screen.blit(text, (600,120))
		#render terrain
		for x in range(len(block_table)):
			for y in range(len(block_table[x])):
				if block_table[y][x] != 0:
					posx   = (x*40)
					posy   = (y*40)
					sizex  = 40
					sizey  = 40
					color  = black
					point1 = (posx - (sizex/2),posy - (sizey/2))
					point2 = (posx + (sizex/2),posy - (sizey/2))
					point3 = (posx + (sizex/2),posy + (sizey/2))
					point4 = (posx - (sizex/2),posy + (sizey/2))
					pygame.draw.polygon(screen,color,(point1,point2,point3,point4))
	def __del__(self):
		pygame.display.flip()

class momentum:
	def __init__(self):
	#momentum for player and other things
		for x in range(len(entity_table)):
			inertx = entity_table[x][3][4][0]
			inerty = entity_table[x][3][4][1]
			posx   = entity_table[x][3][0]
			posy   = entity_table[x][3][1]
			entity_table[x][3][0] = posx + inertx
			entity_table[x][3][1] = posy + inerty
			#slow down for test air resistance x
			if inertx > 0:
				entity_table[x][3][4][0] = inertx - 0.05
			elif inertx < 0:
				entity_table[x][3][4][0] = inertx + 0.05
			#correct for floating point error
			if inertx < 0.05 and inertx > -0.05:
				entity_table[x][3][4][0] = 0
			#slow down for test air resistance y
			if inerty > 0:
				entity_table[x][3][4][1] = inerty - 0.05
			elif inerty < 0:
				entity_table[x][3][4][1] = inerty + 0.05
			#correct for floating point error
			if inerty < 0.05 and inerty > -0.05:
				entity_table[x][3][4][1] = 0
			#gravity
			if inerty < max_velocity:
				entity_table[x][3][4][1] = inerty + 0.1
			

class terraincollision:
	def __init__(self):
		for x in range(len(entity_table)):
			for y in range(len(entity_table)):
				#player
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
				#unoptimized
				#print("blockx:"+str(round(posax/40)))
				#print("blocky:"+str(round(posay/40)))
				on_ground = False
				x_detected = False
				y_detected = False
				for i in range(len(block_table)):
					for z in range(len(block_table[i])):
						if block_table[i][z] != 0:
							
							#terrain
							posbx  = z * 40
							posby  = i * 40
							
							sizebx = 40
							sizeby = 40
							pointb1 = (posbx - (sizebx/2),posby - (sizeby/2))
							pointb2 = (posbx + (sizebx/2),posby - (sizeby/2))
							pointb3 = (posbx + (sizebx/2),posby + (sizeby/2))
							pointb4 = (posbx - (sizebx/2),posby + (sizeby/2))
							topb    = (pointb1[1]+pointb2[1])/2
							bottomb = (pointb3[1]+pointb4[1])/2
							leftb   = (pointb1[0]+pointb4[0])/2
							rightb  = (pointb2[0]+pointb3[0])/2
							#if outside range pass, if in, do bounding box sorting
							if topa > bottomb or bottoma < topb or lefta > rightb or righta < leftb:
								pass
							else:

								xdiff = abs(posax-posbx)
								ydiff = abs(posay-posby)
								if xdiff >= ydiff and x_detected == False:
									x_detected = True
									if posax >= posbx:
										print("X")
										entity_table[0][3][0] = posbx + ((sizeax/2)+(sizebx/2))
										entity_table[x][3][4][0] = 0
										on_ground = True
									if posax < posbx:
										print("X2")
										entity_table[0][3][0] = posbx - ((sizeax/2)+(sizebx/2))
										entity_table[x][3][4][0] = 0
									
								if xdiff < ydiff and y_detected == False:
									y_detected = True
									if posay >= posby:
										print("Y")
										entity_table[0][3][1] = posby + ((sizeay/2)+(sizeby/2))
										entity_table[x][3][4][1] = 0
									if posay < posby:
										print("Y2")
										entity_table[0][3][1] = posby - ((sizeay/2)+(sizeby/2))
										entity_table[x][3][4][1] = 0


w = 0
while w < 2000:
	key = pygame.key.get_pressed()
	control(key)
	momentum()
	terraincollision()
	render(key)

	
