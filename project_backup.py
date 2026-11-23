import pygame
from warehouse import create_warehouse, WAREHOUSE_BOARDS

from bfs import bfs
from ucs import ucs
from astar import astar
pygame.init()
pygame.font.init()
font = pygame.font.SysFont("Arial", 22)
title_font = pygame.font.SysFont("Arial", 28, bold=True)
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

grid, start, goal = create_warehouse()
selected_board = "Board 1 - Easy"

# Calculate grid dimensions automatically
ROWS = len(grid)
COLS = len(grid[0])

CELL_SIZE = 60

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

    # Draw destination first
    row, col = goal

    x = col * CELL_SIZE
    y = row * CELL_SIZE

    pygame.draw.circle(
        screen,
        (220, 50, 50),
        (x + CELL_SIZE // 2, y + CELL_SIZE // 2),
        20
    )

    # Draw robot at its current position
    row, col = robot_position

    x = col * CELL_SIZE
    y = row * CELL_SIZE

    pygame.draw.circle(
        screen,
        GREEN,
        (x + CELL_SIZE // 2, y + CELL_SIZE // 2),
        20
    )


# Draw the path returned by the search algorithm
def draw_path(path):

    # If no path exists, do nothing
    if path is None:
        return

    points = []

    # Convert grid coordinates into pixel coordinates
    for row, col in path:

        x = col * CELL_SIZE + CELL_SIZE // 2
        y = row * CELL_SIZE + CELL_SIZE // 2

        points.append((x, y))

    # Draw a line connecting all path cells
    if len(points) > 1:

        pygame.draw.lines(
            screen,
            (150, 50, 200),
            False,
            points,
            6
        )


def draw_info_panel():

    panel_x = 350
    panel_y = 20
    panel_width = 420
    panel_height = 560

    # Dashboard background
    pygame.draw.rect(
        screen,
        (235, 235, 235),
        (panel_x, panel_y, panel_width, panel_height),
        border_radius=10
    )

    # Dashboard title
    title = title_font.render(
        "Performance Dashboard", True, BLACK
    )
    screen.blit(title, (panel_x + 20, panel_y + 15))

    # Selected board
    board_text = font.render(
        "Board: " + selected_board, True, BLACK
    )
    screen.blit(board_text, (panel_x + 20, panel_y + 65))

    # Selected algorithm
    algorithm_text = font.render(
        "Algorithm: " + selected_algorithm, True, BLACK
    )
    screen.blit(algorithm_text, (panel_x + 20, panel_y + 100))

    # Board selection
    heading = font.render("Change Warehouse:", True, BLACK)
    screen.blit(heading, (panel_x + 20, panel_y + 140))

    board_controls = [
        "Q - Board 1 (Easy)",
        "W - Board 2 (Medium)",
        "E - Board 3 (Hard)"
    ]

    y_position = panel_y + 170

    for item in board_controls:
        text_surface = font.render(item, True, BLACK)
        screen.blit(text_surface, (panel_x + 20, y_position))
        y_position += 28

    # Algorithm selection
    algo_heading = font.render("Run Algorithm:", True, BLACK)
    screen.blit(algo_heading, (panel_x + 20, panel_y + 265))

    algo_controls = [
        "1 - BFS",
        "2 - UCS",
        "3 - A*"
    ]

    y_position = panel_y + 295

    for item in algo_controls:
        text_surface = font.render(item, True, BLACK)
        screen.blit(text_surface, (panel_x + 20, y_position))
        y_position += 27

    # Performance metrics
    metrics_heading = font.render(
        "Performance Metrics:", True, BLACK
    )
    screen.blit(metrics_heading, (panel_x + 20, panel_y + 385))

    if current_metrics is None:

        message = font.render(
            "Run an algorithm to see results", True, BLACK
        )
        screen.blit(message, (panel_x + 20, panel_y + 425))

    else:

        metrics = [
            "Success: " + str(current_metrics["success"]),
            "Time: " + str(round(
                current_metrics["execution_time"] * 1000, 4
            )) + " ms",
            "Explored: " + str(current_metrics["explored_nodes"]),
            "Path Length: " + str(current_metrics["path_length"]),
            "Path Cost: " + str(current_metrics["path_cost"])
        ]

        y_position = panel_y + 425

        for item in metrics:
            text_surface = font.render(item, True, BLACK)
            screen.blit(text_surface, (panel_x + 20, y_position))
            y_position += 25



# Available search algorithms
algorithms = {
    pygame.K_1: ("BFS", bfs),
    pygame.K_2: ("UCS", ucs),
    pygame.K_3: ("A*", astar)
}
# Available warehouse boards
board_keys = {
    pygame.K_q: "Board 1 - Easy",
    pygame.K_w: "Board 2 - Medium",
    pygame.K_e: "Board 3 - Hard"
}

# Current board and algorithm results
selected_board = "Board 1 - Easy"

current_path = None
current_metrics = None
selected_algorithm = "None"

# Robot animation variables
robot_position = start
animation_index = 0
is_animating = False

move_delay = 1000  # Delay between movements in milliseconds
last_move_time = 0

running = True

while running:

    # Handle events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # Check keyboard input
        if event.type == pygame.KEYDOWN:

    # Check whether a board selection key was pressed
            if event.key in board_keys:

                selected_board = board_keys[event.key]

                # Load the selected warehouse
                grid, start, goal = create_warehouse(selected_board)

                # Update grid dimensions
                ROWS = len(grid)
                COLS = len(grid[0])

                # Clear previous algorithm results
                current_path = None
                current_metrics = None
                selected_algorithm = "None"

                # Reset robot and animation
                robot_position = start
                animation_index = 0
                is_animating = False

                print("\nSelected Board:", selected_board)
                print("Start:", start)
                print("Goal:", goal)

            # Check whether an algorithm key was pressed
            elif event.key in algorithms:

                selected_algorithm, algorithm = algorithms[event.key]

                # Execute selected algorithm
                current_path, current_metrics = algorithm(
                    grid,
                    start,
                    goal
                )

                # Reset robot position
                robot_position = start

                # Reset animation
                animation_index = 0

                # Start animation if a path exists
                is_animating = current_path is not None and len(current_path) > 0

                # Record current time
                last_move_time = pygame.time.get_ticks()

                print("\nSelected:", selected_algorithm)
                print("Path:", current_path)
                print("Metrics:", current_metrics)
    
    # Robot movement animation
    if is_animating:

        current_time = pygame.time.get_ticks()

        # Check whether enough time has passed
        if current_time - last_move_time >= move_delay:

            animation_index += 1

            # Check whether robot reached the end
            if animation_index >= len(current_path):

                animation_index = len(current_path) - 1
                is_animating = False

            # Update robot position
            robot_position = current_path[animation_index]
            print("Robot moved to:", robot_position)
            # Update movement time
            last_move_time = current_time

    # Draw everything
    screen.fill(WHITE)

    draw_grid()

    draw_path(current_path)

    draw_markers()

    draw_info_panel()

    pygame.display.update()

pygame.quit()
