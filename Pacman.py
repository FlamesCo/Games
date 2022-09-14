## write pacman game in python3
## import modules
import pygame, sys, random, time
from pygame.locals import *
## initialize pygame
pygame.init()
## set up window
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Pacman')
## set up
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BGCOLOR = BLACK
## make the dots engine
class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = WHITE
        self.size = 5
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
    def draw(self):
        pygame.draw.rect(windowSurface, self.color, self.rect)
## make the pacman engine
class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        ## define YELLOW color 
        self.color = (255, 255, 0)
 
        self.size = 20
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
    def draw(self):
        pygame.draw.rect(windowSurface, self.color, self.rect)
## make the ghost engine
class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = RED
        self.size = 20
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
    def draw(self):
        pygame.draw.rect(windowSurface, self.color, self.rect)
## make the game engine
class Game:
    def __init__(self):
        self.dots = []
        self.pacman = Pacman(100, 100)
        self.ghost = Ghost(200, 200)
        self.score = 0
        self.lives = 3
        self.gameOver = False
        self.gameWon = False
    def draw(self):
        windowSurface.fill(BGCOLOR)
        for dot in self.dots:
            dot.draw()
        self.pacman.draw()
        self.ghost.draw()
        pygame.display.update()
    def run(self):
        while True:
            self.draw()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        self.pacman.x -= 10
                    if event.key == K_RIGHT:
                        self.pacman.x += 10
                    if event.key == K_UP:
                        self.pacman.y -= 10
                    if event.key == K_DOWN:
                        self.pacman.y += 10
## make the game
game = Game()
game.run()
