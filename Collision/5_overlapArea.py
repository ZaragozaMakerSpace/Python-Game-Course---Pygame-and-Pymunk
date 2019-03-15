import pygame, sys, time, random
from pygame.locals import * 
pygame.init()

size = [700, 500]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen= pygame.display.set_mode( size, 0, 32 )
pygame.display.set_caption(' Mask Collision with animation!')

background = pygame.Surface( size )
background_image = pygame.image.load("../rsc/Backgrounds/1_Desert.png").convert()
background_image = pygame.transform.scale(background_image, size )


class Platform(pygame.sprite.Sprite):
	#
	def __init__(self, route):
		#super(Platform, self).__init__()
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(route).convert_alpha()
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface( self.image )

	def set_pos(self, x, y):
		self.x = x
		self.y = y

	def draw( self , surface ):
		surface.blit( self.image, (self.x, self.y ))

	def resize( self , w, h ):
		pass
		#surface.blit(self.image, (self.x, self.y ))

class Player(pygame.sprite.Sprite):
	def __init__(self, route, n_img ):
		#super(Player, self).__init__()
		pygame.sprite.Sprite.__init__(self)
		
		self.route = route
		self.images = []
		self.index = 0
		for x in range(0, n_img):
			self.images.append ( pygame.image.load(self.route+str( x )+'.png').convert_alpha() )

		self.image = self.images[self.index]
		self.mask = pygame.mask.from_surface( self.image )
		self.x = size[0]/2
		self.y = size[1]/2
		self.speed = 8
		self.rect = self.image.get_rect()

	def update(self):
		self.index += 1

		if self.index >= len(self.images):
			self.index = 0

		self.image = self.images[self.index]
		self.mask = pygame.mask.from_surface( self.image )
	
	def move(self):
		""" Handles Keys """
		key = pygame.key.get_pressed()

		dist = self.speed # distance moved in 1 frame, try changing it to 5
		if key[pygame.K_DOWN]: # down key
			self.y += dist # move down
		elif key[pygame.K_UP]: # up key
			self.y -= dist # move up
		if key[pygame.K_RIGHT]: # right key
			self.x += dist # move right
		elif key[pygame.K_LEFT]: # left key
			self.x -= dist # move left

	def set_pos(self, x, y):
		self.x = x
		self.y = y

	def set_speed(self, speed):
		self.speed = speed

	def draw(self, surface):
		surface.blit(self.image, ( self.x , self.y ))

class Sphere(pygame.sprite.Sprite):
	def __init__(self, color, radius, location  ):
		pygame.sprite.Sprite.__init__(self)
		
		self.frame = pygame.Surface( (radius*2 , radius*2) )
		self.frame.fill( (255,255,255))
		self.radius = radius
		self.mask = pygame.mask.from_surface( self.frame)

		pygame.draw.circle( self.frame, color, (radius, radius), radius, 0)
		self.rect = self.frame.get_rect()
		self.rect.topleft = location
		self.speed = [2,2]

	def collide(self, group ):
		impacts = pygame.sprite.spritecollide( self, group, False, pygame.sprite.collide_mask )
		
		for impact in impacts:
			print( impact )
	
		if impacts:
			self.speed[0] = -self.speed[0] 
			self.speed[1] = -self.speed[1] 

	def maskcollide(self, object ):
		impacts = pygame.sprite.collide_mask( self, object )
		
		if impacts:
			print( impacts )
			self.speed[0] = -self.speed[0] 
			self.speed[1] = -self.speed[1] 
	
	def rectcollide(self, group ):
		impacts = pygame.sprite.spritecollide( self, group, False, pygame.sprite.collide_rect )
		
		for impact in impacts:
			print( impact )
	
		if impacts:
			self.speed[0] = -self.speed[0] 
			self.speed[1] = -self.speed[1] 

	def move (self, limits):
		self.rect = self.rect.move(self.speed)
		if self.rect.left < 0 or self.rect.right > limits[0]:
			self.speed[0] = -self.speed[0]
		if self.rect.top < 0 or self.rect.bottom > limits[1]:
			self.speed[1] = -self.speed[1] 

platforms = pygame.sprite.Group()
players = pygame.sprite.Group()

clock = pygame.time.Clock()
base = Platform("../rsc/Object/Various/haycart.png")
base.set_pos(300, 300);
player = Player('../rsc/Player/Pilot/running/frame_',6 )
player.set_pos(200, 200);

platforms.add( base )
players.add( player )

while True: # main game loop 
	screen.blit( background_image, [0,0] )
	clock.tick(30)

	#player.update()
	player.move() 

	base.draw( screen )
	player.draw(screen)

	offset = (base.x - player.x, base.y - player.y)
	result = player.mask.overlap_area(base.mask, offset)

	if result:
		print result

	for event in pygame.event.get():
	
		if event.type == QUIT  or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit() 
			sys.exit()

	pygame.display.update()