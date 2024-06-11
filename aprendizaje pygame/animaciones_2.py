# importamos bibliotecas
import pygame, sys, random

# inicializamos pygame
pygame.init()

# colores
white = (255, 255, 255)
red = (255, 0, 0)

# ventana
size = (800, 500)
screen = pygame.display.set_mode(size)

# nuestro fps
clock = pygame.time.Clock()

# bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(white)
    for lluvia in range(0,61):
        x = random.randint(0, 800)
        y = random.randint(0, 500)
        pygame.draw.circle(screen, red, (x, y), 2)


    # nuestro fondo blanco
        

    #actualizar pygame
    pygame.display.flip()
    clock.tick(60)