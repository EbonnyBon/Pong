import pygame
import sys
import random  # Necesitamos importar el módulo random

pygame.init()

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Definir alto y ancho de jugadores
playerh = 100
playerw = 15

# Pantalla
screen_size = (800, 600)

# Coordenadas del jugador y pelota
player1x = 50
player1y = 300 - 50
splayer1y = 0

player2x = 750 - playerw
player2y = 300 - 50
splayer2y = 0

# Velocidad inicial de la pelota
spelotainicial = 3
spelotaincremento = 0.5

# Definir los FPS
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()

# Estado inicial del juego
gameover = False
paused = False

# Función para reiniciar la pelota en una dirección aleatoria
def reiniciar_pelota():
    global pelotax, pelotay, spelotax, spelotay
    pelotax = 400
    pelotay = 300
    spelotax = spelotainicial * random.choice([-1, 1])  # Elegir al azar entre -1 o 1 para dirección x
    spelotay = spelotainicial * random.choice([-1, 1])  # Elegir al azar entre -1 o 1 para dirección y

# Iniciar el juego con la pelota en una dirección aleatoria
reiniciar_pelota()

while not gameover:
    for event in pygame.event.get():
        # Salir del juego
        if event.type == pygame.QUIT:
            gameover = True
            sys.exit()

        # Controlar movimiento de los jugadores
        if event.type == pygame.KEYDOWN:
            # Jugador 1
            if event.key == pygame.K_w:
                splayer1y = -3
            if event.key == pygame.K_s:
                splayer1y = 3
            # Jugador 2
            if event.key == pygame.K_UP:
                splayer2y = -3
            if event.key == pygame.K_DOWN:
                splayer2y = 3
            # Despausar el juego con Enter
            if paused and event.key == pygame.K_RETURN:
                paused = False

        if event.type == pygame.KEYUP:
            # Jugador 1
            if event.key == pygame.K_w or event.key == pygame.K_s:
                splayer1y = 0
            # Jugador 2
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                splayer2y = 0

    if not paused:
        # Movimiento de los jugadores
        player1y += splayer1y
        player2y += splayer2y

        # Limitar a los jugadores dentro de los bordes de la pantalla
        if player1y < 0:
            player1y = 0
        if player1y > 600 - playerh:
            player1y = 600 - playerh
        if player2y < 0:
            player2y = 0
        if player2y > 600 - playerh:
            player2y = 600 - playerh

        # Movimiento de la pelota
        pelotax += spelotax
        pelotay += spelotay

        # Hacer que la pelota rebote en los bordes superior e inferior
        if pelotay > 590 or pelotay < 10:
            spelotay *= -1

        # Pausar el juego si la pelota sale por los lados
        if pelotax > 800 or pelotax < 0:
            paused = True
            reiniciar_pelota()  # Reiniciar pelota con dirección aleatoria

    # Color de fondo
    screen.fill(BLACK)

    # Dibujar jugadores y pelota
    p1 = pygame.draw.rect(screen, WHITE, (player1x, player1y, playerw, playerh))
    p2 = pygame.draw.rect(screen, WHITE, (player2x, player2y, playerw, playerh))
    plt = pygame.draw.rect(screen, WHITE, (pelotax, pelotay, 10, 10))

    # Colisión de la pelota con los jugadores
    if plt.colliderect(p1) or plt.colliderect(p2):
        spelotax *= -1
        # Aumentar la velocidad gradualmente tras un rebote con los jugadores
        spelotax += spelotaincremento 

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)
