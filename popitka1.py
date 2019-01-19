import pygame


pygame.init()
# размеры окна: 
size = width, height = 800, 600
# screen — холст, на котором нужно рисовать:
screen = pygame.display.set_mode(size)
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
pygame.display.flip()
# ожидание закрытия окна:
while pygame.event.wait().type != pygame.QUIT:
    pass
# завершение работы:
pygame.quit()
