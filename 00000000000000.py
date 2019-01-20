import pygame
import os 

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
image3 = load_image("1547976103654.png")
image = pygame.transform.scale(image3, (220, 220))
screen.blit(image, [270, 50] )
#Рисуем изображение текста на экран в точке (250, 250)
#screen.blit(text, [270, 150] )
# ожидание закрытия окна:
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
# завершение работы:
pygame.quit()
