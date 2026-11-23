import time
from collections import deque


def neighbors(grid, r, c):
    n = len(grid)
    m = len(grid[0])
    result = []
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i, j in moves:
        x = r + i
        y = c + j
        if 0 <= x < n and 0 <= y < m and grid[x][y] != 1:
            result.append((x, y))

    return result 


def cell_cost(value):
    if value == 0:
        return 1
    return value


def bfs(grid, start, goal):
    start_time = time.perf_counter()
    start = tuple(start)
    goal = tuple(goal)

    def metrics(success, explored, length, cost):
        return {
            "algorithm": "BFS",
            "success": success, 
            "execution_time": time.perf_counter() - start_time,
            "explored_nodes": explored,
            "path_length": length,
            "path_cost": cost,
        }

    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return None, metrics(False, 0, 0, None)

    queue = deque([start])
    visited = {start}
    came_from = {}
    explored = 0

    while queue:
        r, c = queue.popleft()
        explored += 1

        if (r, c) == goal:
            path = [goal]
            while path[-1] != start:
                path.append(came_from[path[-1]])
            path.reverse()

            cost = 0
            for pr, pc in path[1:]:
                cost += cell_cost(grid[pr][pc])

            return path, metrics(True, explored, len(path) - 1, cost)

        for neighbor in neighbors(grid, r, c):
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = (r, c)
                queue.append(neighbor)

    return None, metrics(False, explored, 0, None)