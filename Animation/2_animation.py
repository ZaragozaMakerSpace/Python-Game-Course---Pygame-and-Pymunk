import pygame, sys
 
from pygame.locals import * 
pygame.init()

size = [700, 500]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen= pygame.display.set_mode( size )
pygame.display.set_caption('Sprite Class !')

background_image=pygame.image.load("../rsc/Backgrounds/1_Desert.png").convert()
print background_image.get_rect().size 
background_image = pygame.transform.scale(background_image, size )

walk_img  = 6

class Sprite(pygame.sprite.Sprite):
	def __init__(self):
		super(Sprite, self).__init__()
		self.images = []
		self.index = 0
		for x in range(0, walk_img):
			self.images.append ( pygame.image.load('../rsc/Player/Pilot/running/frame_'+str( x )+'.png') )

		self.image = self.images[self.index]

	def update(self):
		self.index += 1

		if self.index >= len(self.images):
			self.index = 0

		self.image = self.images[self.index]

	def draw(self, surface):
		surface.blit(self.image, ( size[0]/2 ,size[1]/2 ))



clock = pygame.time.Clock()

my_sprite = Sprite()


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