import pygame,os ,time
from pygame.locals import (
	QUIT,
	KEYDOWN,
	K_ESCAPE,
	)

screen = pygame.display.set_mode([1000, 500])
pygame.init()
all_sprites = pygame.sprite.Group()

class sprite(pygame.sprite.Sprite):
	def __init__(self,image,scale,position):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load(image),(scale[0],scale[1]))
		self.x = position[0]
		self.y = position[1]
		self.rect = self.image.get_rect()
		self.rect.center = (self.x,self.y)

all_sprites = pygame.sprite.Group()
pn1 = input("First pokemon:  ")
pn2 = input("Second pokemon: ")

overlay = sprite("sprites/overlay.png",[1000,500],[500,250])
sprite1 = sprite("sprites/pokemon/"+pn1+".png",[500,500],[150,250])
sprite2 = sprite("sprites/pokemon/"+pn2+".png",[500,500],[850,250])
sprite3 = sprite("sprites/fusion/"+pn1+"."+pn2+".png",[500,500],[500,250])

all_sprites.add(sprite1)
all_sprites.add(sprite2)
all_sprites.add(sprite3)
all_sprites.add(overlay)

screen.fill((255, 255, 255))
all_sprites.draw(screen)
pygame.display.flip()

while True:
	all_sprites.draw(screen)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()