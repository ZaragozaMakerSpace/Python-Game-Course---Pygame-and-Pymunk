import pygame, sys

from pygame.locals import * 
pygame.init()

size = [700, 500]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen= pygame.display.set_mode( size )
pygame.display.set_caption('Sprite Class with time control elapsed')

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
			img = pygame.image.load(self.route+str( x )+'.png')
			self.images.append ( pygame.transform.scale(img , (50,50) ) )

		self.image = self.images[self.index]
		self.elapsed = pygame.time.get_ticks()
		self.animation_speed = 100

	def animate(self):
		self.index += 1

		if self.index >= len(self.images):
			self.index = 0

		self.image = self.images[self.index]

	def update(self):
		elapsed = pygame.time.get_ticks() - self.elapsed

		if elapsed > self.animation_speed: # animate every half second
			self.elapsed = pygame.time.get_ticks()
			print self.elapsed
			self.animate()

	def set_animation_speed(self, anim_speed ):
		self.animation_speed = anim_speed

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
my_sprite.set_animation_speed( 40 )

while True: # main game loop 
	screen.blit( background_image, [0,0] )
	clock.tick( 100 )

	my_sprite.update()
	my_sprite.move()

	my_sprite.draw(screen)

	for event in pygame.event.get():
		
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit() 
			sys.exit()

	pygame.display.update()