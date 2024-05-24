import pygame
import random

# Initialize Pygame
pygame.init()

# Colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Dimension of the screen
WIDTH = 1350
HEIGHT = 700

# Creating a Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Title
pygame.display.set_caption("Football")

class Ball:
    def __init__(self, x, y):
        self.image = pygame.image.load("player-ship.png")
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_x = 3 * random.choice((1, -1))
        self.speed_y = 3 * random.choice((1, -1))

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y = -1*self.speed_y
    def draw(self):
        screen.blit(self.image, self.rect)
    def reset_ball(self):
        self.rect.x = WIDTH/2
        self.rect.y = HEIGHT/2



class Player:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 0

    def update(self):
        print(self.rect.y)
        keystate  = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed = -8
        if keystate[pygame.K_RIGHT]:
            self.speed = 8
        self.rect.y += self.speed

    def draw(self):
        screen.blit(self.image, self.rect)

class Robot:
    def __init__(self, image_path, x, y, ball):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 0
        self.ball = ball

    def update(self):
        if self.ball.rect.y > self.rect.y:
            self.speed = 2.75
        elif self.ball.rect.y == self.rect.y:
            self.speed = 0
        else:
            self.speed = -2.75
        self.rect.y += self.speed

    def draw(self):
        screen.blit(self.image, self.rect)

ball = Ball(WIDTH // 2, HEIGHT // 2)
player_left = Player("laserred.png", 110, 200)
player_right = Robot("meteor.png", WIDTH - 128 - 110, 200, ball)

class Game:
    global ball, player_right,player_left 
    def __init__(self):
        self.left_player_score = 0
        self.right_player_score = 0
        self.game_font = pygame.font.Font("freesansbold.ttf", 32)

    def update(self):
        ball.update()
        player_left.update()
        player_right.update()

        if ball.rect.left <= 5:
            self.right_player_score += 1
            ball.reset_ball()
        elif ball.rect.right >= WIDTH - 5:
            self.left_player_score += 1
            ball.reset_ball()

    def draw(self):
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, (WIDTH // 2, 3), (WIDTH // 2, HEIGHT - 3), 5)  # MidLine
        pygame.draw.line(screen, WHITE, (3, 3), (WIDTH - 3, 3), 5)  # UpLine
        pygame.draw.line(screen, WHITE, (3, HEIGHT - 5), (WIDTH - 3, HEIGHT - 5), 5)  # DownLine
        pygame.draw.line(screen, WHITE, (5, 1), (5, HEIGHT - 3), 5)  # LeftLine
        pygame.draw.line(screen, WHITE, (WIDTH - 5, 1), (WIDTH - 5, HEIGHT - 3), 5)  # RightLine
        pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 10)  # CentrePoint
        pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 100, 5)  # Centre Circle

        ball.draw()
        player_left.draw()
        player_right.draw()


def main():
    game = Game()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        game.update()

        game.draw()

        pygame.display.flip()

        clock.tick(120)

    pygame.quit()


main()
