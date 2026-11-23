"""A* pathfinding for the Intelligent Warehouse Robot Management System.

Grid convention:
    0 = normal traversable cell (movement cost 1)
    1 = obstacle / shelf (blocked)
    2 = traversable cell (movement cost 2)
    3 = traversable cell (movement cost 3)

Coordinates are (row, column). Movement is up, down, left, or right.

Public interface:
    path, metrics = astar(grid, start, goal)

The metrics dictionary always contains:
    algorithm, success, execution_time, explored_nodes, path_length, path_cost
""" 

import heapq
import time


def heuristic(a, b, min_cost=1):
    """Return an admissible Manhattan-distance heuristic."""
    distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return distance * min_cost


def get_neighbors(grid, current):
    """Return valid, non-obstacle neighboring cells."""
    rows = len(grid)
    cols = len(grid[0])
    row, col = current

    directions = (
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1),   # Right
    )

    neighbors = []
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 1:
            neighbors.append((nr, nc))

    return neighbors


def astar(grid, start, goal):
    """Find a least-cost path using A* Search.

    Args:
        grid: Rectangular 2D list/tuple containing only 0, 1, 2, or 3.
        start: Starting coordinate as (row, column).
        goal: Destination coordinate as (row, column).

    Returns:
        (path, metrics)
        - path is a list of (row, column) tuples, or None if no path exists.
        - metrics is a dictionary with a consistent set of six fields.

    Raises:
        ValueError: If the grid or coordinates are invalid.
    """
    start_time = time.perf_counter()

    # Validate the grid.
    if not isinstance(grid, (list, tuple)) or not grid:
        raise ValueError("Grid cannot be empty")
    if not isinstance(grid[0], (list, tuple)) or not grid[0]:
        raise ValueError("Grid rows cannot be empty")

    rows = len(grid)
    cols = len(grid[0])

    if any(not isinstance(row, (list, tuple)) or len(row) != cols for row in grid):
        raise ValueError("Grid must be rectangular")

    if any(
        type(cell) is not int or cell not in (0, 1, 2, 3)
        for row in grid
        for cell in row
    ):
        raise ValueError("Grid values must be 0, 1, 2, or 3")

    def valid_position(position):
        if not isinstance(position, (tuple, list)) or len(position) != 2:
            return False
        r, c = position
        return (
            type(r) is int
            and type(c) is int
            and 0 <= r < rows
            and 0 <= c < cols
        )

    if not valid_position(start) or not valid_position(goal):
        raise ValueError("Start and goal must be valid (row, column) coordinates")

    start = tuple(start)
    goal = tuple(goal)

    def make_metrics(success, explored_nodes, path_length, path_cost):
        return {
            "algorithm": "A*",
            "success": success,
            "execution_time": time.perf_counter() - start_time,
            "explored_nodes": explored_nodes,
            "path_length": path_length,
            "path_cost": path_cost,
        }

    # A robot cannot start on, or travel to, an obstacle.
    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return None, make_metrics(False, 0, 0, None)

    # The minimum traversable entry cost keeps the heuristic admissible.
    min_cost = min(
        max(1, cell)
        for row in grid
        for cell in row
        if cell != 1
    )

    # Priority queue items: (estimated_total_cost, actual_cost, coordinate).
    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal, min_cost), 0, start))

    came_from = {}
    g_score = {start: 0}
    explored = set()

    while open_list:
        _, current_cost, current = heapq.heappop(open_list)

        # Ignore an outdated queue entry if a better route was found later.
        if current_cost != g_score.get(current):
            continue
        if current in explored:
            continue

        explored.add(current)

        if current == goal:
            path = [goal]
            position = goal
            while position in came_from:
                position = came_from[position]
                path.append(position)
            path.reverse()

            metrics = make_metrics(
                True,
                len(explored),
                len(path) - 1,
                g_score[goal],
            )
            return path, metrics

        for neighbor in get_neighbors(grid, current):
            nr, nc = neighbor
            move_cost = max(1, grid[nr][nc])  # Cost of entering this cell.
            new_cost = g_score[current] + move_cost

            if new_cost < g_score.get(neighbor, float("inf")):
                g_score[neighbor] = new_cost
                came_from[neighbor] = current

                estimated_total = new_cost + heuristic(neighbor, goal, min_cost)
                heapq.heappush(open_list, (estimated_total, new_cost, neighbor))

                # Reopen the node if a better route to it is discovered.
                explored.discard(neighbor)

    return None, make_metrics(False, len(explored), 0, None)
