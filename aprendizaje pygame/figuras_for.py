# plantilla

# librerias
import pygame, sys

# inicializamos la libreria
pygame.init()


# definimos colores 
# simplemente sistema de colores del RGB
BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED =   ( 255,   0,   0)
BLUE = (   0,   0,  255)

# tamaño de la ventana
size = (800, 500) # ancho, alto

# la ventana
screen = pygame.display.set_mode(size)

# bucle principal
while True:
    # registro de eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
    # a partir de esta identacion se continua el juego

    # color de la ventana
    screen.fill(WHITE)

    # zona de dibujo

    #  este for genrera 6 cuadros de color negro 
    for x in range(100, 700, 100):
        pygame.draw.rect(screen, BLACK, (x, 230, 50, 50))
    
    # zona de dibujo
    
    pygame.display.flip()
