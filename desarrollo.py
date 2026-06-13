import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración de pantalla
ANCHO = 650
ALTO = 650
TAM_CELDA = 20

pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Snake Game")

# Colores
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
BLANCO = (255, 255, 255)

# Reloj
clock = pygame.time.Clock()
FPS = 10

# Fuente
fuente = pygame.font.SysFont(None, 35)


def mostrar_puntaje(puntaje):
    texto = fuente.render(f"Tu puntaje obtenido: {puntaje}", True, BLANCO)
    pantalla.blit(texto, (10, 10))


def generar_comida():
    x = random.randrange(0, ANCHO, TAM_CELDA)
    y = random.randrange(0, ALTO, TAM_CELDA)
    return [x, y]


# Snake inicial
snake = [[100, 100], [80, 100], [60, 100]]
direccion = "RIGHT"

comida = generar_comida()
puntaje = 0

while True:
    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP and direccion != "DOWN":
                direccion = "UP"
            elif evento.key == pygame.K_DOWN and direccion != "UP":
                direccion = "DOWN"
            elif evento.key == pygame.K_LEFT and direccion != "RIGHT":
                direccion = "LEFT"
            elif evento.key == pygame.K_RIGHT and direccion != "LEFT":
                direccion = "RIGHT"

    # Mover cabeza
    cabeza = snake[0][:]

    if direccion == "UP":
        cabeza[1] -= TAM_CELDA
    elif direccion == "DOWN":
        cabeza[1] += TAM_CELDA
    elif direccion == "LEFT":
        cabeza[0] -= TAM_CELDA
    elif direccion == "RIGHT":
        cabeza[0] += TAM_CELDA

    snake.insert(0, cabeza)

    # Comer comida
    if cabeza == comida:
        puntaje += 1
        comida = generar_comida()
    else:
        snake.pop()

    # Colisión con paredes
    if (
        cabeza[0] < 0 or cabeza[0] >= ANCHO or
        cabeza[1] < 0 or cabeza[1] >= ALTO
    ):
        break

    # Colisión consigo misma
    if cabeza in snake[1:]:
        break

    # Dibujar
    pantalla.fill(NEGRO)

    # Comida
    pygame.draw.rect(
        pantalla,
        ROJO,
        (comida[0], comida[1], TAM_CELDA, TAM_CELDA)
    )

    # Snake
    for segmento in snake:
        pygame.draw.rect(
            pantalla,
            VERDE,
            (segmento[0], segmento[1], TAM_CELDA, TAM_CELDA)
        )

    mostrar_puntaje(puntaje)

    pygame.display.update()
    clock.tick(FPS)

# Pantalla final
pantalla.fill(NEGRO)
texto = fuente.render(
    f"Game Over - Puntaje: {puntaje}",
    True,
    BLANCO
)
pantalla.blit(texto, (120, ALTO // 2))
pygame.display.update()
pygame.time.wait(3000)

pygame.quit()