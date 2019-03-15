import pygame, sys, time, random
import numpy
from pygame.locals import * 
pygame.init()

size = [700, 500]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

screen= pygame.display.set_mode( size, 0, 32 )
pygame.display.set_caption('Events in customizable Button!')

background = pygame.Surface( size )
background_image = pygame.image.load("../rsc/Backgrounds/1_Desert.png").convert()
background_image = pygame.transform.scale(background_image, size )

def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if click[0]:
		print msg+'Button pressed'

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

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
			
			if self.index == 0: 
				olist = numpy.array( self.mask.outline() )
				olist = olist + (self.x, self.y)
				pygame.draw.lines(screen,(125,255,0),1,olist, 5)

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

clock = pygame.time.Clock()

UI_newGame = UI('../rsc/UI/NewGame/frame_',6 )
UI_newGame.set_pos(200, 200);

while True: # main game loop 
	screen.blit( background_image, [0,0] )
	clock.tick(10)
	button( "GO!",100,100,100,50,GREEN,WHITE )

	UI_newGame.update()
	UI_newGame.draw(screen)

	mouse_pos = pygame.mouse.get_pos()
	
	rel_pos = mouse_pos[0]-UI_newGame.x,  mouse_pos[1] - UI_newGame.y
	
	rect = UI_newGame.rect
	
	collision = rect.collidepoint(rel_pos)

	if collision:
		UI_newGame.set_over(False)
		click = pygame.mouse.get_pressed()
		if click[0]:
			print 'PRESSED'
	else:
		UI_newGame.set_over(True)
	
	for event in pygame.event.get():
	
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit() 
			sys.exit()
	
	pygame.display.update()