import pygame
import random

# Initialize Pygame
pygame.init()

# Colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (100, 255, 100)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Dimension of the screen
WIDTH = 1350
HEIGHT = 700

# Creating a Screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Title
pygame.display.set_caption("Football")

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ball.png")
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_x = 3 * random.choice((1, -1))
        self.speed_y = 3 * random.choice((1, -1))

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y = -self.speed_y
            if self.speed_y > 0:
                self.speed_y += 0.25
            else:
                self.speed_y -= 0.25
        print(self.speed_y)



    def draw(self):
        screen.blit(self.image, self.rect)

    def reset_ball(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = 3 * random.choice((1, -1))
        self.speed_y = 3 * random.choice((1, -1))

    def hit(self):
        self.speed_x = -self.speed_x


class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 0

    def update(self):
        keystate = pygame.key.get_pressed()
        self.speed = 0
        if keystate[pygame.K_UP]:
            self.speed = -8
        if keystate[pygame.K_DOWN]:
            self.speed = 8
        self.rect.y += self.speed

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self):
        screen.blit(self.image, self.rect)


class Robot(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, ball):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 0
        self.ball = ball

    def update(self):
        if self.ball.rect.y > self.rect.y:
            self.speed = 4
        elif self.ball.rect.y < self.rect.y:
            self.speed = -4
        else:
            self.speed = 0
        self.rect.y += self.speed

        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def draw(self):
        screen.blit(self.image, self.rect)


class Game:
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
            if self.right_player_score == 3:
                running = False

        elif ball.rect.right >= WIDTH - 5:
            self.left_player_score += 1
            ball.reset_ball()
            if self.left_player_score == 3:
                running = False

    def draw(self):
        screen.fill(GREEN)
        pygame.draw.line(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 5)  # MidLine
        pygame.draw.line(screen, WHITE, (0, 0), (WIDTH, 0), 5)  # UpLine
        pygame.draw.line(screen, WHITE, (0, HEIGHT), (WIDTH, HEIGHT), 5)  # DownLine
        pygame.draw.line(screen, WHITE, (0, 0), (0, HEIGHT), 5)  # LeftLine
        pygame.draw.line(screen, WHITE, (WIDTH, 0), (WIDTH, HEIGHT), 5)  # RightLine
        pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 10)  # CentrePoint
        pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 100, 5)  # Centre Circle

        ball.draw()
        player_left.draw()
        player_right.draw()

        left_score_text = self.game_font.render(str(self.left_player_score), True, WHITE)
        right_score_text = self.game_font.render(str(self.right_player_score), True, WHITE)
        screen.blit(left_score_text, (WIDTH // 4, 20))
        screen.blit(right_score_text, (WIDTH * 3 // 4, 20))


ball = Ball(WIDTH // 2, HEIGHT // 2)
player_left = Player("player_1.png", 110, HEIGHT // 2)
player_right = Robot("player_2.png", WIDTH - 128 - 110, HEIGHT // 2, ball)

all_sprites = pygame.sprite.Group()
all_sprites.add(player_left)
all_sprites.add(player_right)
all_sprites.add(ball)

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

        if pygame.sprite.collide_rect(player_left, ball):
            ball.hit()

        if pygame.sprite.collide_rect(player_right, ball):
            ball.hit()

        pygame.display.flip()
        clock.tick(120)

        if game.left_player_score == 3:
                running = False
        if game.right_player_score == 3:
                running = False

    pygame.quit()

main()
