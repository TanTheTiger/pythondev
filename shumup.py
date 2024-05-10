import pygame
import time
import random

Width = 800
Height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,165,0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Pygame")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(player_img, (50,38))
		self.rect = self.image.get_rect()
		self.rect.centerx = (Width/2)
		self.rect.bottom = Height - 20
		self.speedx = 0

	def update(self):
		self.speedx = 0
		keystate  = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speedx = -8
		if keystate[pygame.K_RIGHT]:
			self.speedx = 8

		self.rect.x += self.speedx

		if self.rect.right > Width:
			self.rect.right = Width
		if self.rect.left < 0:
			self.rect.left = 0
	def shoot(self):
		bullet = Bullet(self.rect.centerx, self.rect.top)
		all_sprites.add(bullet)
		bullets.add(bullet)
		shoot_sound.play()

class Mob(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = meteor_img
		self.rect = self.image.get_rect()
		self.rect.x = random.randrange(0,Width - self.rect.width)
		self.rect.y = random.randrange(-100,-40)
		self.speedx = random.randrange(-3,3)
		self.speedy = random.randrange(1,8)

	def update(self):
		self.rect.x += self.speedx
		self.rect.y += self.speedy
		if self.rect.top > Height + 10 or self.rect.left < -25 or self.rect.right > Width + 20:
			self.rect.x = random.randrange(Width - self.rect.width)
			self.rect.y = random.randrange(-100,-40)
			self.speedy = random.randrange(1,8)

class Bullet(pygame.sprite.Sprite):
	def __init__(self, x,y):
		pygame.sprite.Sprite.__init__(self)
		self.image = bullet_img  
		self.rect = self.image.get_rect()
		self.rect.bottom = y
		self.rect.centerx = x
		self.speedy = -10

	def update(self):
		self.rect.y += self.speedy
		if self.rect.bottom < 0:
			self.kill()

background = pygame.image.load("starfield.png")
background_rect = background.get_rect()
player_img = pygame.image.load("player-ship.png")
meteor_img = pygame.image.load("meteor.png")
bullet_img = pygame.image.load("laserred.png")

shoot_sound = pygame.mixer.Sound('Laser_Shoot4.wav')

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
bullets = pygame.sprite.Group()
mobs = pygame.sprite.Group()


for i in range(8):
	m = Mob()
	all_sprites.add(m)
	mobs.add(m)
running = True
while running:
	clock.tick(30)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				player.shoot()

	hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
	for hit in hits:
		m = Mob()
		all_sprites.add(m)
		mobs.add(m)

	hits = pygame.sprite.spritecollide(player,mobs,False)
	if hits:
		running = False

	screen.fill(black)
	screen.blit(background,background_rect)
	all_sprites.update()
	all_sprites.draw(screen)
	pygame.display.flip()
pygame.quit()
