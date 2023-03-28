import pygame
from pygame.locals import *
import time
import random

size = 40


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.x = 2*size
        self.y = 2*size
        self.image = pygame.image.load("images/apple.jpg").convert()

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()


class Snake():
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.length = length
        self.direction = ''
        self.x = [size]*length
        self.y = [size]*length
        self.block = pygame.image.load("images/block.jpg").convert()

    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)


    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))


    def move(self):
        for i in range(self.length-1, 0, -1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        if self.direction == 'down':
            self.y[0] += size
        if self.direction == 'up':
            self.y[0] -= size
        if self.direction == 'left':
            self.x[0] -= size
        if self.direction == 'right':
            self.x[0] += size
        self.draw()


class Game():
    def __init__(self):
        self.screen = pygame.display.set_mode((1000, 600))
        self.screen.fill((110, 110, 5))
        self.snake = Snake(self.screen, 1)
        self.snake.draw()
        self.apple = Apple(self.screen)
        self.apple.draw()
        self.hit = ''

    def is_collision(self, x1, x2, y1, y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
        return False

    def play(self):
        self.snake.move()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()
        if self.is_collision(self.apple.x, self.snake.x[0], self.apple.y, self.snake.y[0]):
            self.apple.x = size * random.randint(0, 24)
            self.apple.y = size * random.randint(0, 14)
            self.snake.increase_length()


    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"SCORE: {self.snake.length}", True, (255, 255, 255))
        self.screen.blit(score, (800, 10))

    def run(self):
        pygame.init()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_DOWN and self.snake.direction != 'up':
                        self.snake.direction = 'down'
                    if event.key == K_UP and self.snake.direction != 'down':
                        self.snake.direction = 'up'
                    if event.key == K_RIGHT and self.snake.direction != 'left':
                        self.snake.direction = 'right'
                    if event.key == K_LEFT and self.snake.direction != 'right':
                        self.snake.direction = 'left'
                    if event.key == K_SPACE:
                        time.sleep(199999)
                elif event.type == QUIT:
                    running = False
            self.play()
            time.sleep(0.2)


if __name__ == "__main__":
    game = Game()
    game.run()







