
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
'''font = pygame.font.Font(None, 60)
text = font.render("Math Drive", True, (255, 99, 17))'''

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
image3 = load_image("C:/Users/dbobi/Documents/гуки/1547976103654.png")
image = pygame.transform.scale(image3, (220, 220))
screen.blit(image, [270, 50] )
#Рисуем изображение текста на экран в точке (250, 250)
#screen.blit(text, [270, 150] )
# ожидание закрытия окна:
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    running = True
    while running:
     for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
    
      if event.type == pygame.MOUSEBUTTONDOWN:
 
        if event.button == 3:
            pygame.init()
            # размеры окна: 
            size = width, height = 800, 600
            # screen — холст, на котором нужно рисовать:
            screen = pygame.display.set_mode(size)
            screen.fill((135, 206, 250))
            font = pygame.font.Font(None, 60)
            text = font.render("Инструкция", True, (255, 99, 17))
            font1 = pygame.font.Font(None, 30)
            text1 = font1.render("Привет!",True, (255, 99, 17))

            text2 = font1.render("Что это?",True, (255, 99, 17))
            text3 = font1.render(' Это обучающая игра "Math Drive" для развития твоих ',True, (255, 99, 17))
            text4 = font1.render('интеллектуальных способностей.Она поможет тебе быстрее вычислять ',True, (255, 99, 17))
            text5 = font1.render('различные примеры из таблицы умножения что очень пригодится тебе ',True, (255, 99, 17))
            text6 = font1.render('в дальнейшем на уроках математики.',True, (255, 99, 17))

            text7 = font1.render("Как играть?",True, (255, 99, 17))
            text8 = font1.render('Передвигай машинку вверх и вниз, используя кнопки, чтобы перейти ', True, (255, 99, 17))
            text9 = font1.render('на ряд с нужным ответом на пример в облачке наверху.Думай быстро ', True, (255, 99, 17))
            text10 = font1.render('и у тебя всё получится!', True, (255, 99, 17))
            #Рисуем изображение текста на экран в точке (250, 250)
            screen.blit(text, [200, 50] )
            screen.blit(text1, [50, 150] )
            screen.blit(text2, [50, 180] )
            screen.blit(text3, [50, 210] )
            screen.blit(text4, [50, 240] )
            screen.blit(text5, [50, 270] )
            screen.blit(text6, [50, 300] )
            screen.blit(text7, [50, 400] )
            screen.blit(text8, [50, 450] )
            screen.blit(text9, [50, 480] )
            screen.blit(text10, [50, 510] )
            # ожидание закрытия окна:
            pygame.display.flip()
            while pygame.event.wait().type != pygame.QUIT:
                pass
            # завершение работы:
           
            pygame.quit()

        if event.button == 1:

                                          #  левая кнопка мыши
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
                        o2 = ['16','67','43','26','31','84','66','90','8','3','20','13']
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
                            image3 = load_image("C:/Users/dbobi/Documents/гуки/poloska.png")
                            
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
                        image2 = load_image1("C:/Users/dbobi/Documents/гуки/2.png")
                        image = pygame.transform.scale(image2, (220, 220))
                        pygame.draw.circle(screen, (255, 255, 255), (x1, y1), 30, 0)
                        x = 0
                        t = 0
                        m = 0
                        n = str(0)
                        y = 290
                        x1 = 750
                        screen.blit(image, [x, y] )
                        b = 20
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
                            if b == 20:
                                b -= 20
                                font = pygame.font.Font(None, 60)
                                t = v.index(random.choice(v))
                                text = font.render(v[t], True, (255, 99, 17))
                                screen.blit(text, [590, 40])
                                ot = [o[t], o1[t], o2[t]]
                                q = random.choice(ot)
                                ind = ot.index(q)
                                del ot[ind]
                                q1 = random.choice(ot)
                                ind = ot.index(q1)
                                del ot[ind]
                                q2 = ''.join(ot)        
                            else:
                                b += 1
                                screen.blit(text, [590, 40])
                                if x1 >= 0:
                                    x1 -= 30
                                else:
                                    x1 = 750
                            pygame.draw.circle(screen, (178, 34, 34), (x1, 210), 30, 0)
                            pygame.draw.circle(screen, (178, 34, 34), (x1, 380), 30, 0)
                            pygame.draw.circle(screen, (178, 34, 34), (x1, 500), 30, 0)
                            font1 = pygame.font.Font(None, 60)
                            text1 = font1.render(q, True, (255, 99, 17))
                            screen.blit(text1, [x1 - 20, y1-27])
                            font2 = pygame.font.Font(None, 60)
                            text2 = font2.render(q1, True, (255, 99, 17))
                            screen.blit(text2, [x1 - 20, 360])
                            font3 = pygame.font.Font(None, 60)
                            text3 = font3.render(q2, True, (255, 99, 17))
                            screen.blit(text3, [x1 - 30, 490])     
                            pygame.draw.circle(screen, (255, 255, 255), (350, 90), 55, 0)
                            pygame.draw.circle(screen, (255, 255, 255), (380, 85), 67, 0)
                            pygame.draw.circle(screen, (255, 255, 255), (450, 90), 55, 0)
                            all_sprites.draw(screen)
                            image2 = load_image1("C:/Users/dbobi/Documents/гуки/2.png")
                            image = pygame.transform.scale(image2, (220, 220))
                            screen.blit(image, [x, y] )
                            if q == o[t] and y == 160 and x1 == 100:
                                m += 100
                                n = str(m)
                                font4 = pygame.font.Font(None, 60)
                                text4 = font4.render(n, True, (255, 99, 17))
                                screen.blit(text4, [400, 50])         
                            elif q1 == o[t] and y == 290 and x1 == 100:
                                m += 100
                                n = str(m)
                                font4 = pygame.font.Font(None, 60)
                                text4 = font4.render(n, True, (255, 99, 17))
                                screen.blit(text4, [400, 50])         
                            elif q2 == o[t] and y == 420 and x1 == 100:
                                m += 100
                                n = str(m)
                                font4 = pygame.font.Font(None, 60)
                                text4 = font4.render(n, True, (255, 99, 17))
                                screen.blit(text4, [400, 50])        
                            font4 = pygame.font.Font(None, 60)
                            text4 = font4.render(n, True, (255, 99, 17))
                            screen.blit(text4, [400, 50])
                            all_sprites.update()    
                            pygame.display.flip()
                        
                # завершение работы:
                        pygame.quit()
                        exit()
