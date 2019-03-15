import pygame, sys, time, random
import numpy
from pygame.locals import * 
pygame.init()

size = [700, 500]
HW, HH = size[0] / 2, size[1] / 2

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
		self.image = pygame.transform.scale2x( pygame.image.load(route).convert_alpha() )
		self.rect = self.image.get_rect()
		self.mask = pygame.mask.from_surface( self.image )
		self.ox = HW - self.rect.center[0]
		self.oy = HH - self.rect.center[1]

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
			self.images.append ( pygame.transform.scale2x( pygame.image.load(self.route+str( x )+'.png').convert_alpha() ) )

		self.image = self.images[self.index]
		self.mask = pygame.mask.from_surface( self.image )
		self.x = size[0]/2
		self.y = size[1]/2
		self.speed = 15
		self.rect = self.image.get_rect()
		self.ox = HW - self.rect.center[0]
		self.oy = HH - self.rect.center[1]

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
	clock.tick( 10 )

	player.move() 
	player.update()

	base.draw( screen )
	player.draw(screen)

	
	olist = numpy.array(player.mask.outline())
	olist = olist + (player.x, player.y)

	pygame.draw.lines( screen ,(255,0,0),1,olist, 3)

	offset = (base.x - player.x, base.y - player.y)
	result =  player.mask.overlap(base.mask, offset) 
	
	if result:
		print result
		surf = numpy.array(result)
		surf += ( player.x, player.y )

		pygame.draw.circle( screen, (0,0,255) , surf, 10, 3 )


	for event in pygame.event.get():
	
		if event.type == QUIT  or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit() 
			sys.exit()

	
	pygame.display.update()