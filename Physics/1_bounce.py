# Library imports
import pygame, sys
from pygame.key import *
from pygame.locals import *
from pygame.color import *

# pymunk imports
import pymunk
import pymunk.pygame_util
from pymunk import Vec2d


size = [700, 500]

space = pymunk.Space()
space.gravity = (0.0, -9.80)

pygame.init()
screen = pygame.display.set_mode( size )
draw_options = pymunk.pygame_util.DrawOptions( screen )
pymunk.pygame_util.positive_y_is_up = True

background_image=pygame.image.load("../rsc/Backgrounds/Desert.png").convert()
background_image = pygame.transform.scale(background_image, size )

static_body = space.static_body

#Ball

mass = 10
radius = 25
inertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
body = pymunk.Body(mass, inertia)
body.position = 50, size[1]-50

shape = pymunk.Circle(body, radius, (0, 0))
shape.elasticity = 0.95
shape.friction = 0.9

space.add(body, shape)
image = pygame.image.load("../Pilot/running/frame_0.png")

dt = 1.0 / 60.0
physics_steps_per_frame = 1

#Floor
static_line = pymunk.Segment(static_body, (0, 0), ( size[0],0), 2.0)
static_line.elasticity = 0.95
static_line.friction = 0.9
space.add(static_line)

while True:
	screen.blit( background_image, [0,0] )

	for x in range( physics_steps_per_frame):
		space.step( dt)
		pass

	collision = shape.shapes_collide(static_line)
	if collision.points:
		print collision

	p = pymunk.pygame_util.from_pygame( body.position,  screen ) - Vec2d(radius,  radius)

	space.debug_draw( draw_options)
	screen.blit(image, p  )
	pygame.display.flip()

	for event in pygame.event.get():

		if event.type == QUIT  or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit() 
			sys.exit()

		key = pygame.key.get_pressed()
		if key[pygame.K_SPACE]: 
			body.apply_impulse_at_local_point(pymunk.Vec2d(0, 500), (0, 0))
			pass