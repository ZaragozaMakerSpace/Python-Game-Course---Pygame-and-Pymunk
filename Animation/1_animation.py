import pygame, sys
 
from pygame.locals import * 
pygame.init()

size = [700, 500]

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen= pygame.display.set_mode( size )
pygame.display.set_caption('First Animation!')

background_image=pygame.image.load("../rsc/Backgrounds/1_Desert.png").convert()
print background_image.get_rect().size 
background_image = pygame.transform.scale(background_image, size )

walk_img  = 19

walk_sprite = [ ]

for x in range(0, walk_img):
	img = pygame.image.load('../rsc/Player/Pilot/jump/frame_'+str( x )+'.png')
	walk_sprite.append (  pygame.transform.scale(img , (50,50) ) )

actual_img = 0

clock = pygame.time.Clock()
tamanio =  50
while True: # main game loop 
	screen.blit( background_image, [0,0] )
	img = walk_sprite[ actual_img ]
	screen.blit(   pygame.transform.scale( img , (tamanio,tamanio)) , [ size[0]/2 ,size[1]/2] )
	
	actual_img+=1

	if actual_img >=  walk_img :
		actual_img = 0

	clock.tick(10)

	for event in pygame.event.get():
		key = pygame.key.get_pressed()
		if key[pygame.K_DOWN]: 
			tamanio =  50
		if key[pygame.K_UP]:
			 tamanio =  100
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit() 
			sys.exit()
	pygame.display.update()
	





	