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

circle_color = (255, 0, 0)
circle_position = [400, 300]  # Ahora usamos una lista para permitir la modificación
circle_radius = 50
velocity = 5
# la ventana
screen = pygame.display.set_mode(size)

# esta funcion controla los FPS
clock = pygame.time.Clock()

# bucle principal
while True:
    # registro de eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # a partir de esta identacion se continua el juego


    # le damos la funcion de deteccion de teclado 
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        circle_position[0] -= velocity
    if keys[pygame.K_RIGHT]:
        circle_position[0] += velocity
    if keys[pygame.K_UP]:
        circle_position[1] -= velocity
    if keys[pygame.K_DOWN]:
        circle_position[1] += velocity
    ''' creamos las condiciones para que el 
    el script detecte que se estan presionando 
    las teclas '''

   

    # acualizacion de la pantalla 
    
    
    
    pygame.draw.circle(screen, circle_color, circle_position, circle_radius)
    pygame.display.flip()
     # ajustamos a 20 FPS el juego
    clock.tick(60)