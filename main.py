import pygame
from pygame.locals import *
import time

size = 40


class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.x = size*4
        self.y = size*4
        self.block = pygame.image.load("images/apple.jpg").convert()

    def draw(self):
        self.parent_screen.blit(self.block, (self.x, self.y))
        pygame.display.flip()


class Snake():
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.length = length
        self.x = [size]*length
        self.y = [size]*length
        self.block = pygame.image.load("images/block.jpg").convert()
        self.direction = ''

    def draw(self):
        self.parent_screen.fill((110, 110, 5))
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        pygame.display.flip()

    def move(self):
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == 'DOWN':
            self.y[0] += size
        if self.direction == 'UP':
            self.y[0] -= size
        if self.direction == 'LEFT':
            self.x[0] -= size
        if self.direction == 'RIGHT':
            self.x[0] += size

        self.draw()


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))
        self.screen.fill((110, 110, 5))
        self.snake = Snake(self.screen, 3)
        self.snake.draw()
        self.apple = Apple(self.screen)
        self.apple.draw()

    def play(self):
        self.snake.move()
        self.apple.draw()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_DOWN and self.snake.direction != 'UP':
                        self.snake.direction = 'DOWN'
                    if event.key == K_UP and self.snake.direction != 'DOWN':
                        self.snake.direction = 'UP'
                    if event.key == K_RIGHT and self.snake.direction != 'LEFT':
                        self.snake.direction = 'RIGHT'
                    if event.key == K_LEFT and self.snake.direction != 'RIGHT':
                        self.snake.direction = 'LEFT'

                if event.type == QUIT:
                    running = False
            self.play()
            time.sleep(0.2)


if __name__ == "__main__":
    game = Game()
    game.run()







