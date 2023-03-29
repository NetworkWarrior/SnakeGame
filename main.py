import pygame
from pygame.locals import *
import time
import random

size = 40

background_color = (81, 156, 83)
class Apple:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.x = 2*size
        self.y = 2*size
        self.image = pygame.image.load("images/apple.jpg").convert()

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        pygame.display.flip()

    def move_apple(self):
        self.x = size * random.randint(0,24)
        self.y = size * random.randint(2,14)

class Snake():
    def __init__(self, parent_screen, length):
        self.parent_screen = parent_screen
        self.length = length
        self.direction = 'right'
        self.x = [size]*length
        self.y = [size]*length
        self.block = pygame.image.load("images/block.jpg").convert()

    def increase_length(self):
        self.length += 1
        self.x.append(6)
        self.y.append(6)


    def draw(self):
        self.parent_screen.fill((background_color))
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
        pygame.init()
        pygame.mixer.init()
        self.background_music()
        self.screen = pygame.display.set_mode((1000, 600))
        self.screen.fill((background_color))
        self.snake = Snake(self.screen, 2)
        self.snake.draw()
        self.apple = Apple(self.screen)
        self.apple.draw()
        self.hit = ''


    def is_collision(self, x1, x2, y1, y2):
        if x1 >= x2 and x1 < x2 + size:
            if y1 >= y2 and y1 < y2 + size:
                return True
        return  False

    def background_music(self):
        pygame.mixer.music.load("images/518917__bloodpixelhero__the-calm-theme.wav")
        pygame.mixer.music.play()

    def apple_snake_crash(self):
        crash = False
        for i in range(self.snake.length - 1, 0, -1):
            if self.apple.x == self.snake.x[i] and self.apple.y == self.snake.y[i]:
                crash = True
                break
        return crash


    def play(self):
        self.snake.move()
        self.apple.draw()
        self.display_score()
        pygame.display.flip()
        # eating apples
        if self.is_collision(self.apple.x, self.snake.x[0], self.apple.y, self.snake.y[0]):
            sound = pygame.mixer.Sound("images/632232__audacitier__biting-apple-1.mp3")
            pygame.mixer.Sound.play(sound)
            self.apple.move_apple()
            self.snake.increase_length()
        while self.apple_snake_crash():
            self.apple.move_apple()
        # collision of snake body
        for i in range(3, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.x[i], self.snake.y[0], self.snake.y[i]):
                sound = pygame.mixer.Sound("images/cymbal-crash-sound-effect.mp3")
                pygame.mixer.Sound.play(sound)
                raise "game over!"
        if (1000 <= self.snake.x[0] or self.snake.x[0] < 0) or (600 <= self.snake.y[0] or self.snake.y[0] < 0):
            sound = pygame.mixer.Sound("images/cymbal-crash-sound-effect.mp3")
            pygame.mixer.Sound.play(sound)
            raise  "game over!!"

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"SCORE: {self.snake.length-2}", True, (255, 255, 255))
        self.screen.blit(score, (800, 10))

    def show_game_over(self):
        pygame.mixer.music.pause()
        self.screen.fill((background_color))
        font = pygame.font.SysFont("arial", 30)
        line1 = font.render(f"GAME OVER!! : {self.snake.length-2}", True, (255, 255, 255))
        self.screen.blit(line1, (300, 200))
        line2 = font.render(f"HIT ENTER TO RESTART OR ESC TO EXIT", True, (255, 255, 255))
        self.screen.blit(line2, (300, 300))
        pygame.display.flip()

    def reset(self):
        self.snake = Snake(self.screen, 2)
        self.apple = Apple(self.screen)


    def run(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        self.background_music()
                        pause = False
                    if not pause:
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
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause = True
                self.reset()
            time.sleep(.1)


if __name__ == "__main__":
    game = Game()
    game.run()







