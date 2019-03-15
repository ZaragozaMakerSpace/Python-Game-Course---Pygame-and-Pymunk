import pygame, sys

from pygame.locals import * 
pygame.init()

size = [700, 500]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen= pygame.display.set_mode( size )
pygame.display.set_caption('Sprite Class Multiplayer Movements!')

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
		self.position = [0, 0]
		self.velocity = 1
		self.ctrl_up = pygame.K_UP
		self.ctrl_down = pygame.K_DOWN
		self.ctrl_left = pygame.K_LEFT
		self.ctrl_right = pygame.K_RIGHT

	def animate(self):
		self.index += 1

		if self.index >= len(self.images):
			self.index = 0

		self.image = self.images[self.index]

	def update(self):
		elapsed = pygame.time.get_ticks() - self.elapsed

		if elapsed > self.animation_speed: # animate every half second
			self.elapsed = pygame.time.get_ticks()
			self.animate()
	
	def set_pos(self, x, y):
		self.position[0] = x
		self.position[1] = y

	def set_animation_speed(self, anim_speed ):
		self.animation_speed = anim_speed

	def set_controls(self, ctrl_up, ctrl_down, ctrl_left, ctrl_right ):
		self.ctrl_up = ctrl_up
		self.ctrl_down = ctrl_down
		self.ctrl_left = ctrl_left
		self.ctrl_right = ctrl_right

	def draw(self, surface):
		surface.blit(self.image, ( self.position[0] , self.position[1] ))

	def move(self):
		""" Handles Keys """
		key = pygame.key.get_pressed()

		if key[ self.ctrl_down ]: # down key
			self.position[1] += self.velocity
			pass
		elif key[ self.ctrl_up ]: # up key
			self.position[1] -= self.velocity
			pass
		if key[ self.ctrl_right ]: # right key
			self.position[0] += self.velocity
			pass
		elif key[ self.ctrl_left ]: # left key
			self.position[0] -= self.velocity
			pass

clock = pygame.time.Clock()

player1 = Sprite('../rsc/Player/Pilot/running/frame_',6 )
player1.set_animation_speed( 50 )
player1.set_pos( 100,100 )

player2 = Sprite('../rsc/Player/Pilot/running/frame_',6 )
player2.set_animation_speed( 100 )
player2.set_pos( 200,200 )
player2.set_controls(   pygame.K_w , pygame.K_s, pygame.K_a, pygame.K_d )

while True: # main game loop 
	screen.blit( background_image, [0,0] )
	clock.tick( 100 )

	player1.update()
	player1.move()
	player1.draw(screen)

	player2.update()
	player2.move()
	player2.draw(screen)

	for event in pygame.event.get():
		
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit() 
			sys.exit()

	pygame.display.update()