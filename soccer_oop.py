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
        self.speed_x = 1.5 * random.choice((1, -1))
        self.speed_y = 1.5

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.right >= WIDTH - 5 or self.rect.left <= 5:
            self.speed_x *= -1

        if self.rect.bottom <= HEIGHT or self.rect.top > 0:
            self.speed_y *= -1

    def draw(self):
        screen.blit(self.image, self.rect)


class Player:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 0

    def update(self):
        self.rect.y += self.speed
        if self.rect.top <= 5:
            self.rect.top = 5
        elif self.rect.bottom >= HEIGHT - 5:
            self.rect.bottom = HEIGHT - 5

    def draw(self):
        screen.blit(self.image, self.rect)

"""
class Robot:
    def __init__(self, image_path, x, y):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = 0

    def update(self):
        self.rect.y += self.speed
        if self.rect.top <= 5:
            self.rect.top = 5
        elif self.rect.bottom >= HEIGHT - 5:
            self.rect.bottom = HEIGHT - 5

    def draw(self):
        screen.blit(self.image, self.rect)
"""

class Game:
    def __init__(self):
        self.ball = Ball(WIDTH // 2, HEIGHT // 2)
        self.player_left = Player("laserred.png", 110, 200)
        self.player_right = Player("meteor.png", WIDTH - 128 - 110, 200)
        self.left_player_score = 0
        self.right_player_score = 0
        self.game_font = pygame.font.Font("freesansbold.ttf", 32)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.player_left.top -= 2
                elif event.key == pygame.K_d:
                    self.player_left.top += 2
                elif event.key == pygame.K_w:
                    self.player_right.speed -= 2
                elif event.key == pygame.K_s:
                    self.player_right.speed += 2
                
    def update(self):
        self.ball.update()
        self.player_left.update()
        self.player_right.update()

        if self.ball.rect.left <= 5:
            self.right_player_score += 1
            self.reset_ball()
        elif self.ball.rect.right >= WIDTH - 5:
            self.left_player_score += 1
            self.reset_ball()

    def draw(self):
        screen.fill(BLACK)
        pygame.draw.line(screen, WHITE, (WIDTH // 2, 3), (WIDTH // 2, HEIGHT - 3), 5)  # MidLine
        pygame.draw.line(screen, WHITE, (3, 3), (WIDTH - 3, 3), 5)  # UpLine
        pygame.draw.line(screen, WHITE, (3, HEIGHT - 5), (WIDTH - 3, HEIGHT - 5), 5)  # DownLine
        pygame.draw.line(screen, WHITE, (5, 1), (5, HEIGHT - 3), 5)  # LeftLine
        pygame.draw.line(screen, WHITE, (WIDTH - 5, 1), (WIDTH - 5, HEIGHT - 3), 5)  # RightLine
        pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 10)  # CentrePoint
        pygame.draw.circle(screen, WHITE, (WIDTH // 2, HEIGHT // 2), 100, 5)  # Centre Circle

        # Display scores
        player_a_text = self.game_font.render(str(self.left_player_score), True, BLUE)
        player_b_text = self.game_font.render(str(self.right_player_score), True, BLUE)
        screen.blit(player_a_text, (WIDTH // 2 - 75 - 40, 600))
        screen.blit(player_b_text, (WIDTH // 2 + 75, 600))

        # Draw players and ball
        self.ball.draw()
        self.player_left.draw()
        self.player_right.draw()

    def reset_ball(self):
        self.ball.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.ball.speed_x = random.choice((1, -1))
        self.ball.speed_y = random.choice((1, -1))


def main():
    game = Game()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.handle_events()

        game.update()

        game.draw()

        pygame.display.flip()

        clock.tick(120)

    pygame.quit()


if __name__ == "__main__":
    main()
