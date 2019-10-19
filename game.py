import pygame, sys
from pygame.locals import *
import boid as rules

# create boids
class Boid():
    def __init__(self,position,velocity):
        self.position = position # (x, y)
        self.velocity = velocity # (dx, dy)

    def update(self, newPosition, newVelocity):
        self.oldPosition = self.position
        self.oldVelocity = self.velocity
        self.position = newPosition
        self.velocity = newVelocity

        x,y = self.oldPosition
        oldPos = int(x), int(y)

        x,y = self.position
        pos = int(x), int(y)

        pygame.draw.circle(DISPLAYSURF, WHITE, oldPos, 3)
        pygame.draw.circle(DISPLAYSURF, RED, pos, 3)

    def destroy(self):
        pygame.draw.circle(DISPLAYSURF, WHITE, self.position, 3)

pygame.init()
size = width, height = 500,500
DISPLAYSURF = pygame.display.set_mode(size)
pygame.display.set_caption('Commuter Chaos')

DISPLAYSURF.fill((255,255,255))

WHITE = (255,255,255)
BLACK = (0,0,0)
RED   = (255,0,0)

# create a city layout with block size of 100, spacing of 50
blockSize = 100
spacing = 50
buildings = [(i,j,blockSize,blockSize) for i in range(spacing,width,blockSize+spacing) for j in range(spacing,height,blockSize + spacing)]

# buildings = [(10,10,40,40),(60,10,40,40),(10,60,40,40),(60,60,40,40)]
for building in buildings:
    pygame.draw.rect(DISPLAYSURF,BLACK,building)

# create a bunch of boids
boids = [Boid((100+i*10,100+j*10),(0,0)) for i in range(5) for j in range(5)]
# boids = [Boid((250,250),(0,0)), Boid((250,255),(0,0))]

while True:#
    rules.moveallboids(boids)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
#    pygame.time.Clock().tick(60)
