import pygame, sys, time, random
from pygame.locals import * 
pygame.init()

size = [700, 500]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen= pygame.display.set_mode( size, 0, 32 )
pygame.display.set_caption('Spheres Collision!')

background = pygame.Surface( size )
background_image = pygame.image.load("../rsc/Backgrounds/1_Desert.png").convert()
background_image = pygame.transform.scale(background_image, size )


class Sphere(pygame.sprite.Sprite):
	def __init__(self, color, radius, location ):
		#super(Sphere, self).__init__()
		pygame.sprite.Sprite.__init__(self)
		
		self.frame = pygame.Surface( (radius*2 , radius*2), pygame.SRCALPHA, 32)
		self.frame = self.frame.convert_alpha()

		pygame.draw.circle( self.frame, color, (radius, radius), radius, 0)
		self.rect = self.frame.get_rect()
		self.radius = radius
		self.rect.topleft = location
		self.speed = [2,2]

	def collide(self, enemy):
		
		impacts = pygame.sprite.collide_circle( self, enemy )
	
		if impacts:
			print 'Ouch'
			self.speed[0] = -self.speed[0] 
			self.speed[1] = -self.speed[1] 
			enemy.speed[0] = -enemy.speed[0] 
			enemy.speed[1] = -enemy.speed[1] 

	def move (self, limits):
		self.rect = self.rect.move(self.speed)
		if self.rect.left < 0 or self.rect.right > limits[0]:
			self.speed[0] = -self.speed[0]
		if self.rect.top < 0 or self.rect.bottom > limits[1]:
			self.speed[1] = -self.speed[1] 


spheres = pygame.sprite.Group()

locations = [ ( 100, 100 ), ( 200 , 200 ), ( 300 , 300 ), ( 100, 250 ) ]

clock = pygame.time.Clock()

enemyball = Sphere( (0,0,0), 40, (200,400) ) 
for x in locations:
	color = ( random.randint(1,255), random.randint(1,255), random.randint(1,255) )
	radius = 25
	ball = Sphere( color, radius, x ) 
	spheres.add(ball)

while True: # main game loop 
	screen.blit( background_image, [0,0] )
	clock.tick(30)
	enemyball.move( size ) 
	screen.blit(enemyball.frame, enemyball.rect)
	
	for ball in spheres:
		ball.move( size ) 
		spheres.remove(ball) #No debe detectarse a si misma dentro de la lista de esferas, por lo que eliminamos de la lista
		
		ball.collide( enemyball )
		spheres.add(ball) #Y la aniadimos a la lista de nuevo para la siguiente operacion del bucle
		screen.blit(ball.frame, ball.rect)

	for event in pygame.event.get():
	
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit() 
			sys.exit()

	pygame.display.update()