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
size = (800, 800) #ancho, alto

# la ventana
screen = pygame.display.set_mode(size)

# esta funcion controla los FPS
clock = pygame.time.Clock()
# coordenadas del cuadro 
cord_x = 400
cord_y = 200

# velocidad de la animacion
speed_x = 3 
speed_y = 3

# bucle principal
while True:
    # registro de eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # esta funcion evita que nuestra animacion salga de la pantalla
        if (cord_x > 800 or cord_x < 0):
            speed_x *= -1
        
        if (cord_y > 800 or cord_y < 0):
            speed_y *= -1

        
    # a partir de esta identacion se continua el juego

    # le sumamos la velocidada a la cordenada X
    cord_x += speed_x
    cord_y += speed_y

    screen.fill(WHITE)
    # zona de dibujo

    #generamos una linea                  eje:x  eje:y
    pygame.draw.rect(screen, RED, (cord_x, cord_y, 80, 80))

    

    #zona de dibujo 

    # acualizacion de la pantalla 
    pygame.display.flip()

    # ajustamos a 20 FPS el juego
    clock.tick(60)















