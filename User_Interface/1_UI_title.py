import pygame, sys, time, random
from pygame.locals import * 
pygame.init()

size = [700, 500]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen= pygame.display.set_mode( size, 0, 32 )
pygame.display.set_caption('Detecting Touch Overlap with mouse and Title Animation!')

background = pygame.Surface( size )
background_image = pygame.image.load("../rsc/Backgrounds/1_Desert.png").convert()
background_image = pygame.transform.scale(background_image, size )


class UI(pygame.sprite.Sprite):
	def __init__(self, route, n_img ):
		pygame.sprite.Sprite.__init__(self)
		
		self.route = route
		self.images = []
		self.index = 0
		for x in range(0, n_img):
			self.images.append ( pygame.image.load(self.route+str( x )+'.gif').convert_alpha() )

		self.image = self.images[self.index]
		self.mask = pygame.mask.from_surface( self.image )
		self.x = size[0]/2
		self.y = size[1]/2
		self.speed = 8
		self.rect = self.image.get_rect()
		self.over = False

	def update(self):
		
		if self.over:

			if self.index < len( self.images )-1: 
				self.index += 1
		else:
			if self.index > 0: 
				self.index -= 1

		self.image = self.images[self.index]
		self.mask = pygame.mask.from_surface( self.image )

	def set_over(self, over):
		self.over = over

	def set_pos(self, x, y):
		self.x = x
		self.y = y

	def set_speed(self, speed):
		self.speed = speed

	def draw(self, surface):
		surface.blit(self.image, ( self.x , self.y ))

#UIGroup = pygame.sprite.Group()

clock = pygame.time.Clock()

UI_newGame = UI('../rsc/UI/NewGame/frame_',6 )
UI_newGame.set_pos(200, 200);

#UIGroup.add( UI_newGame )

while True: # main game loop 
	screen.blit( background_image, [0,0] )
	clock.tick(10)

	UI_newGame.update()
	UI_newGame.draw(screen)

	mouse_pos = pygame.mouse.get_pos()
	
	rel_pos = mouse_pos[0]-UI_newGame.x,  mouse_pos[1] - UI_newGame.y

	mask = UI_newGame.mask
	try: 
		#Si se encuentra fuera de los limites de la mascara no lo reconoce como parte de la mascara
		collision = mask.get_at(rel_pos)
		if collision:
			UI_newGame.set_over(True)
		else:
			UI_newGame.set_over(False)
	except IndexError: 
		pass	

	for event in pygame.event.get():
	
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit() 
			sys.exit()

	pygame.display.update()