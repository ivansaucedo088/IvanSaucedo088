#simplemente para que funcione el juego, usamos la libreria "pygame"
# e importamos la libreria sys, para evitar errores fururos
import pygame, sys

# para inicializar la libreria usamos :
pygame.init()

# aqui definimos el tamaño de la ventana

size = (800, 500) # (ancho, alto)

# aqui se ejecuta la ventana
screen = pygame.display.set_mode(size) 

''' lo juegos siempre se ejecuntan dentro de un bucle'''
while True:
    #esto registra todos los eventos del juego 
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit
    pass    
