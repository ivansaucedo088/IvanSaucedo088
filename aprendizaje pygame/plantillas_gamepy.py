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

# esta funcion controla los FPS
clock = pygame.time.Clock()

# bucle principal
while True:
    # registro de eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
    # a partir de esta identacion se continua el juego


    # acualizacion de la pantalla 
    pygame.display.flip()

     # ajustamos a 20 FPS el juego
    clock.tick(60)