"""
warehouse.py
Member 1: Warehouse Environment & Problem Formulation
 
Grid values:
    0 = Empty cell (movement cost 1)
    1 = Obstacle / shelf (blocked)
    2 = Terrain cost 2
    3 = Terrain cost 3

Coordinates are (row, column).
Robot movement: Up, Down, Left, Right only.
"""

# Sample 5 x 5 warehouse map.
# You can change the positions of shelves and terrain as needed.

# Multiple warehouse boards

WAREHOUSE_BOARDS = {

    "Board 1 - Easy": {
        "grid": [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ],
        "start": (0, 0),
        "goal": (4, 4)
    },

    "Board 2 - Medium": {
        "grid": [
            [0, 0, 0, 1, 0],
            [0, 2, 0, 1, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 3, 2, 0],
            [0, 0, 0, 0, 0]
        ],
        "start": (0, 0),
        "goal": (4, 4)
    },

    "Board 3 - Hard": {
        "grid": [
            [0, 1, 0, 0, 0],
            [0, 2, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 3, 0, 2, 0],
            [0, 0, 0, 0, 0]
        ],
        "start": (0, 0),
        "goal": (4, 4)
    }
}


# Possible robot actions: (row change, column change)
ACTIONS = {
    "UP": (-1, 0),
    "DOWN": (1, 0),
    "LEFT": (0, -1),
    "RIGHT": (0, 1)
}


def validate_warehouse(grid, start, goal):
    """Check whether the grid and start/goal positions are valid."""
    if not isinstance(grid, (list, tuple)) or len(grid) == 0:
        raise ValueError("Warehouse grid cannot be empty.")

    if not isinstance(grid[0], (list, tuple)) or len(grid[0]) == 0:
        raise ValueError("Warehouse rows cannot be empty.")

    rows = len(grid)
    cols = len(grid[0])

    if any(not isinstance(row, (list, tuple)) or len(row) != cols
           for row in grid):
        raise ValueError("Warehouse grid must be rectangular.")

    for row in grid:
        for cell in row:
            if type(cell) is not int or cell not in (0, 1, 2, 3):
                raise ValueError("Grid cells must contain only 0, 1, 2, or 3.")

    def valid_position(position):
        return (
            isinstance(position, (tuple, list))
            and len(position) == 2
            and type(position[0]) is int
            and type(position[1]) is int
            and 0 <= position[0] < rows
            and 0 <= position[1] < cols
        )

    if not valid_position(start):
        raise ValueError("Start must be a valid (row, column) position.")

    if not valid_position(goal):
        raise ValueError("Goal must be a valid (row, column) position.")

    if grid[start[0]][start[1]] == 1:
        raise ValueError("The robot cannot start on an obstacle.")

    if grid[goal[0]][goal[1]] == 1:
        raise ValueError("The destination cannot be an obstacle.")

    return True


def get_neighbors(grid, position):
    """Return all valid cells reachable in one move from position."""
    rows = len(grid)
    cols = len(grid[0])
    r, c = position
    result = []

    # The order is Up, Down, Left, Right.
    for dr, dc in ACTIONS.values():
        nr = r + dr
        nc = c + dc

        if (0 <= nr < rows and 0 <= nc < cols
                and grid[nr][nc] != 1):
            result.append((nr, nc))

    return result


def get_cell_cost(grid, position):
    """Return the cost of entering a cell. Obstacles are not traversable."""
    r, c = position
    value = grid[r][c]

    if value == 1:
        raise ValueError("An obstacle cannot be entered.")

    return max(1, value) 



def create_warehouse(board_name="Board 1 - Easy"):
    """Return a fresh copy of the selected warehouse board."""

    if board_name not in WAREHOUSE_BOARDS:
        raise ValueError("Invalid warehouse board selected.")

    board = WAREHOUSE_BOARDS[board_name]

    grid = [row[:] for row in board["grid"]]
    start = board["start"]
    goal = board["goal"]

    validate_warehouse(grid, start, goal)

    return grid, start, goal



def display_warehouse(grid, start=None, goal=None, path=None):
    """Print the warehouse; S=start, G=goal, *=path, #=shelf."""
    path_cells = set(path) if path else set()

    print("\nWarehouse map:")
    print("S = Start | G = Goal | # = Shelf | * = Path")
    for r in range(len(grid)):
        row_display = []
        for c in range(len(grid[0])):
            position = (r, c)

            if position == start:
                symbol = "S"
            elif position == goal:
                symbol = "G"
            elif position in path_cells:
                symbol = "*"
            elif grid[r][c] == 1:
                symbol = "#"
            else:
                symbol = str(grid[r][c])

            row_display.append(symbol)

        print(" ".join(row_display))


if __name__ == "__main__":

    for board_name in WAREHOUSE_BOARDS:

        print("\n==========================")
        print(board_name)
        print("==========================")

        grid, start, goal = create_warehouse(board_name)

        print("Start:", start)
        print("Goal:", goal)

        display_warehouse(grid, start, goal)