

import pygame

pygame.init()

# Window dimensions
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Warehouse Robot Simulator")

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (190, 190, 190)
BLUE = (50, 120, 220)
GREEN = (50, 200, 100)
YELLOW = (240, 200, 50)

# Warehouse grid
grid = [
    [0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0],
    [1, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 2, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

ROWS = len(grid)
COLS = len(grid[0])

CELL_SIZE = 60

# Robot starting position
start = (0, 0)

# Delivery destination
goal = (7, 7)

# Draw warehouse
def draw_grid():

    for row in range(ROWS):

        for col in range(COLS):

            x = col * CELL_SIZE
            y = row * CELL_SIZE

            cell = grid[row][col]

            if cell == 0:
                color = WHITE

            elif cell == 1:
                color = BLACK

            elif cell == 2:
                color = YELLOW

            elif cell == 3:
                color = BLUE

            pygame.draw.rect(
                screen,
                color,
                (x, y, CELL_SIZE, CELL_SIZE)
            )

            pygame.draw.rect(
                screen,
                GRAY,
                (x, y, CELL_SIZE, CELL_SIZE),
                1
            )


def draw_markers():

    # Robot position
    row, col = start

    x = col * CELL_SIZE
    y = row * CELL_SIZE

    pygame.draw.circle(
        screen,
        GREEN,
        (x + CELL_SIZE // 2, y + CELL_SIZE // 2),
        20
    )

    # Destination position
    row, col = goal

    x = col * CELL_SIZE
    y = row * CELL_SIZE

    pygame.draw.circle(
        screen,
        (220, 50, 50),
        (x + CELL_SIZE // 2, y + CELL_SIZE // 2),
        20
    )



running = True

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    draw_grid()
    draw_markers()

    pygame.display.update()

pygame.quit()
