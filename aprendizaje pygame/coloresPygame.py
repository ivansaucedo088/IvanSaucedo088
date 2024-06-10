import pygame, sys

pygame.init()

''' en esta seccion se aprendera a dibujar formas'''

# definimos colores 
# simplemente sistema de colores del RGB
BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED =   ( 255,   0,   0)
BLUE = (   0,   0,  255)

size = (800, 500)

screen = pygame.display.set_mode(size) 

''' lo juegos siempre se ejecuntan dentro de un bucle'''
while True:
    #esto registra todos los eventos del juego 
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
    
    # la identacion siempre tiene que ir en el for
    

    # el fondo de la pantalla sera blanca
    screen.fill(WHITE) 

    # ZONA DE DIBUJO

    #creamos una linea
    pygame.draw.line(screen, GREEN, [0, 100], [100, 100], 5)
    ''' el primer argumento es donde se va a dibujar
    la linea (screen)

    punto inicio y final (0, 100)

    la orientación (100, 100) * horizontalmente

    despues cual es su grosor (5)
    '''

    # otro ejemplo con un rectangulo 

    pygame.draw.rect(screen, BLUE, (110, 100, 100, 100))

    # ZONA DE DIBIJO

    # este metodo actualiza la pantalla
    pygame.display.flip() 
