import os 
import pygame.key
import pygame
import copy
import random
import sys


pygame.init()
# размеры окна: 
size = width, height = 800, 600
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
screen.fill((135, 206, 250))
flag = False
pygame.draw.line(screen, (34, 139, 34), (0, 210), (800, 210), 30)
pygame.draw.line(screen, (255, 255, 255), (0, 230), (800, 230), 9)
pygame.draw.line(screen, (128, 128, 128), (0, 414), (800, 414), 360)
pygame.draw.line(screen, (255, 255, 255), (0, 360), (800, 360), 9)
pygame.draw.line(screen, (255, 255, 255), (0, 480), (800, 480), 9)
pygame.draw.line(screen, (255, 255, 255), (0, 595), (800, 595), 9)
pygame.draw.circle(screen, (255, 255, 255), (85, 60), 30, 0)
pygame.draw.circle(screen, (255, 255, 255), (120, 55), 40, 0)
pygame.draw.circle(screen, (255, 255, 255), (150, 60), 30, 0)
pygame.draw.circle(screen, (255, 255, 255), (600, 60), 30, 0)
pygame.draw.circle(screen, (255, 255, 255), (630, 55), 40, 0)
pygame.draw.circle(screen, (255, 255, 255), (680, 60), 30, 0)
pygame.draw.circle(screen, (255, 255, 255), (350, 90), 55, 0)
pygame.draw.circle(screen, (255, 255, 255), (400, 85), 67, 0)
pygame.draw.circle(screen, (255, 255, 255), (450, 90), 55, 0)


def load_image1(name1, colorkey=None):
    fullname1 = os.path.join('data', name1)
    try:
        image1 = pygame.image.load(fullname1)
    except pygame.error as message:
        print('Cannot load image1:', name1)
        raise SystemExit(message)
    image1 = image1.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image1.set_colorkey(colorkey)
    return image1

class Bomb1(pygame.sprite.Sprite):
    image2 = load_image1("2.png")
    image = pygame.transform.scale(image2, (220, 220))
    
    def __init__(self, group):
            # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
            # Это очень важно!!!
            super().__init__(group)
            self.image = Bomb1.image
            self.rect = self.image.get_rect()
            self.rect.x = 0
            self.rect.y = 290
    
    def update(self):
        pass
    
    def up(self):
        super().__init__()
        self.rect.x = 0
        self.rect.y = 260
               
    
    def get_event(self, event):
            
            if self.rect.collidepoint(event.pos):
                self.image1= self.image1_boom 
            
    
    
all_sprites1 = pygame.sprite.Group()
    
for i in range(20):
    Bomb1(all_sprites1)


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image

class Bomb(pygame.sprite.Sprite):
    image3 = load_image("poloska.png")
    image = pygame.transform.scale(image3, (100, 10))
    
    def __init__(self, group):
            # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
            # Это очень важно!!!
            super().__init__(group)
            self.image = Bomb.image
            self.rect = self.image.get_rect()
            self.rect.x = 800
            self.rect.y = random.choice([300, 425, 550])
    
    def update(self):

        if self.rect.x >= 0:
            self.rect = self.rect.move(random.randrange(2) - 2, 0)
        else:
            self.rect.x =  800
            self.rect.y = random.choice([300, 425, 550])
            
    def get_event(self, event):
            
            if self.rect.collidepoint(event.pos):
                self.image = self.image_boom 
            
    
    
all_sprites = pygame.sprite.Group()
    
for i in range(20):
    Bomb(all_sprites)


running = True
pressed_keys = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False            
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_SPACE:
                bomb = Bomb1(1)
                bomb.up()
            fire()
    screen.fill((135, 206, 250))
    pygame.draw.line(screen, (34, 139, 34), (0, 210), (800, 210), 30)
    pygame.draw.line(screen, (255, 255, 255), (0, 230), (800, 230), 9)
    pygame.draw.line(screen, (128, 128, 128), (0, 414), (800, 414), 360)
    pygame.draw.line(screen, (255, 255, 255), (0, 360), (800, 360), 9)
    pygame.draw.line(screen, (255, 255, 255), (0, 480), (800, 480), 9)
    pygame.draw.line(screen, (255, 255, 255), (0, 595), (800, 595), 9)
    pygame.draw.circle(screen, (255, 255, 255), (85, 60), 30, 0)
    pygame.draw.circle(screen, (255, 255, 255), (120, 55), 40, 0)
    pygame.draw.circle(screen, (255, 255, 255), (150, 60), 30, 0)
    pygame.draw.circle(screen, (255, 255, 255), (600, 60), 30, 0)
    pygame.draw.circle(screen, (255, 255, 255), (630, 55), 40, 0)
    pygame.draw.circle(screen, (255, 255, 255), (680, 60), 30, 0)
    pygame.draw.circle(screen, (255, 255, 255), (350, 90), 55, 0)
    pygame.draw.circle(screen, (255, 255, 255), (400, 85), 67, 0)
    pygame.draw.circle(screen, (255, 255, 255), (450, 90), 55, 0)
    all_sprites.draw(screen)
    all_sprites1.draw(screen)
    all_sprites.update()
    all_sprites1.update()     
    pygame.display.flip()
pygame.quit()
