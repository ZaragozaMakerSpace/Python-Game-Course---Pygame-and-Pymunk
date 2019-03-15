import pygame, sys

from pygame.locals import * 
pygame.init()

size = [700, 500]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen= pygame.display.set_mode( size )
pygame.display.set_caption('Sprite Class with args and move Method!')

background_image=pygame.image.load("../rsc/Backgrounds/1_Desert.png").convert()
print background_image.get_rect().size 
background_image = pygame.transform.scale(background_image, size )

class Sprite(pygame.sprite.Sprite):
	def __init__(self, route, n_img ):
		super(Sprite, self).__init__()
		self.route = route
		self.images = []
		self.index = 0
		for x in range(0, n_img):
			self.images.append ( pygame.image.load(self.route+str( x )+'.png') )

		self.image = self.images[self.index]

	def update(self):
		self.index += 1

		if self.index >= len(self.images):
			self.index = 0

		self.image = self.images[self.index]

	def draw(self, surface):
		surface.blit(self.image, ( size[0]/2 ,size[1]/2 ))

	def move(self):
		""" Handles Keys """
		key = pygame.key.get_pressed()
		dist = 0.1 # distance moved in 1 frame, try changing it to 5
		if key[pygame.K_DOWN]: # down key
			pass
		elif key[pygame.K_UP]: # up key
			pass
		if key[pygame.K_RIGHT]: # right key
			pass	
		elif key[pygame.K_LEFT]: # left key
			pass

clock = pygame.time.Clock()

my_sprite = Sprite('../rsc/Player/Pilot/running/frame_',6 )


while True: # main game loop 
	screen.blit( background_image, [0,0] )
	clock.tick(10)

	my_sprite.update()
	my_sprite.draw(screen)

	for event in pygame.event.get():
		
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit() 
			sys.exit()

	pygame.display.update()