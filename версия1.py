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
v = ['2*2','3*3','4*4','5*5','4*7','3*7','7*7','6*7','7*8','4*6','6*9','9*9']
o = ['4','9','16','25','28','21','49','42','56','24','54','81']
o1 = ['13','20','47','22','32','59','19','1','91','100','23','50']
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
            self.rect = self.rect.move(random.randrange(2) - 200, 0)
        else:
            self.rect.x =  800
            self.rect.y = random.choice([300, 425, 550])
            
    def get_event(self, event):
            
            if self.rect.collidepoint(event.pos):
                self.image = self.image_boom 
            
    
    
all_sprites = pygame.sprite.Group()
x1 = 750
y1 = 230  
for i in range(20):
    Bomb(all_sprites)

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
image2 = load_image1("2.png")
image = pygame.transform.scale(image2, (220, 220))
pygame.draw.circle(screen, (255, 255, 255), (x1, y1), 30, 0)
x = 0
t = 0
y = 290
x1 = 750
y1 = 210
screen.blit(image, [x, y] )
b = 11
running = True
while running:
    if x1 == 0:
        x1 == 800
    else:
        x1 -= 10
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False            
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_UP:
                y -= 130
            if event.key ==  pygame.K_DOWN:
                y += 130
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
    pygame.draw.circle(screen, (255, 255, 255), (x1, y1), 30, 0)
    if b == 11:
        b -= 11
        font = pygame.font.Font(None, 60)
        t = v.index(random.choice(v))
        text = font.render(v[t], True, (255, 99, 17))
        screen.blit(text, [590, 40])
    else:
        b += 1
        screen.blit(text, [590, 40])
        if x1 != 0:
            x1 -= 30
        else:
            x1 = 750
    pygame.draw.circle(screen, (178, 34, 34), (x1, y1), 30, 0)
    font1 = pygame.font.Font(None, 60)
    text1 = font1.render(o[t], True, (255, 99, 17))
    screen.blit(text1, [x1, y1])    
    pygame.draw.circle(screen, (255, 255, 255), (350, 90), 55, 0)
    pygame.draw.circle(screen, (255, 255, 255), (400, 85), 67, 0)
    pygame.draw.circle(screen, (255, 255, 255), (450, 90), 55, 0)
    all_sprites.draw(screen)
    image2 = load_image1("2.png")
    image = pygame.transform.scale(image2, (220, 220))
    screen.blit(image, [x, y] )
    all_sprites.update()    
    pygame.display.flip()
pygame.quit()
