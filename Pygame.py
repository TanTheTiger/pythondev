import pygame
import time
import random

pygame.init()

Width = 800
Height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption("Pygame")

font_style = pygame.font.SysFont("comicsansms", 30)
score_style = pygame.font.SysFont("bahnschrift", 30)

def scr(score):
	value = score_style.render("Your Score: "+str(score),True,green)
	screen.blit(value, [10,10])

def message(msg,color,xpos,ypos):
	sty=font_style.render(msg, True, color)
	screen.blit(sty,[xpos,ypos])

def our_snake(snake_size, snake_list):
	for x in snake_list:
		pygame.draw.rect(screen, green,[x[0],x[1],snake_size,snake_size])


def gameloop():
	gameover = False
	x = Width/2
	y = Height/2
	snake_size = 20
	xchg = 0
	ychg = 0
	size = 20
	fx = round(random.randrange(0,Width-size)/10)*10
	fy = round(random.randrange(0,Height-size)/10)*10
	font1 = pygame.font.SysFont('freesanbold.ttf',50)
	snake_list = []
	len_snake = 1

	running = False
	clock = pygame.time.Clock()
	while not gameover:

		while running == True:
			screen.fill(blue)
			message("You lost! Press Q to Quit or C to Play Again", red,0,300)
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						running = False
						gameover = True
					if event.key == pygame.K_c:
						gameloop()
		clock.tick(15)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameover = False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					screen.blit(text,textrect)
				if event.key == pygame.K_LEFT:
					xchg-=10
					ychg = 0
			
				if event.key == pygame.K_RIGHT:
					xchg+=10
					ychg = 0
				
				if event.key == pygame.K_UP:
					ychg-=10
					xchg=  0
		
				if event.key == pygame.K_DOWN:
					ychg+=10
					xchg = 0
					
		x+=xchg
		y+=ychg
		screen.fill(blue)
		snake_head  =[]
		snake_head.append(x)
		snake_head.append(y)
		snake_list.append(snake_head)

		if len(snake_list)>len_snake:
			del snake_list[0]

		for i in snake_list[-1]:
			if i == snake_head:
				running = True
		our_snake(snake_size,snake_list)
		scr(len_snake-1)
		pygame.draw.rect(screen, green,[x,y,snake_size,snake_size])
		pygame.draw.rect(screen,red,[fx,fy,size,size])
		if x >= Width or x<0 or y>= Height or y<0:
			running = True
		pygame.display.update()
		if x == fx and y == fy:
			fx = round(random.randrange(0,Width-size)/10)*10
			fy = round(random.randrange(0,Height-size)/10)*10
			len_snake+=1
	pygame.quit()
	quit()
gameloop()
pygame.quit()
