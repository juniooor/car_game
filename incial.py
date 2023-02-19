import random
import sys

import pygame
from pygame.locals import *

pygame.init()

FPS = 30
FramePerSec = pygame.time.Clock()
#cores predefinidas

blue  = (0, 0, 255)
red  = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(white)
pygame.display.set_caption("Game")
DEFAULT_IMAGE_SIZE = (70,90) 
enemy = pygame.image.load("enemy2.png")
car = pygame.image.load("car2.png")
enemy_image = pygame.transform.scale(enemy, DEFAULT_IMAGE_SIZE)
player_image = pygame.transform.scale(car, DEFAULT_IMAGE_SIZE)
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = enemy_image
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 
 
      def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
      def draw(self, surface):
        surface.blit(self.image, self.rect) 
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = player_image
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
                self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect)     
 
         
P1 = Player()
E1 = Enemy()
 
while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    E1.move()
     
    DISPLAYSURF.fill(white)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
         
    pygame.display.update()
    FramePerSec.tick(FPS)