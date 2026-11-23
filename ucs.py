import heapq
import time

def cost(n):
    if n == 0:
        return 1 
    return n

def metrics(name,success,explored,length,total,t):
    return {
        "algorithm" : name,
        "success" : success, 
        "execution_time" : time.perf_counter() - t,
        "explored_nodes" : explored,
        "path_length" : length,
        "path_cost" : total
    }

def successors(grid,state):

    r,c = state
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    give = list()

    for i,j in moves:
        x = r + i
        y = c + j
        if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]) and grid[x][y] != 1:
            give.append((x,y))

    return give

def show(path,m):

    print(f"\n----- {m['algorithm']} -----\n")

    if path is None:
        print("No possible solution!!")
    else:
        print(f"Path Found !!!! at cost = {m['path_cost']}\n")
        for x in path:
            print(x)
            print("\n")

    print(f"Explored nodes : {m['explored_nodes']}")
    print(f"Path length    : {m['path_length']}")
    print(f"Path cost      : {m['path_cost']}")
    print(f"Execution time : {m['execution_time']:.8f} s")

def ucs(grid,start,goal):

    t = time.perf_counter()
    start = tuple(start)
    goal = tuple(goal)

    if grid[start[0]][start[1]] == 1 or grid[goal[0]][goal[1]] == 1:
        return None,metrics("UCS",False,0,0,None,t)

    open = []
    heapq.heappush(open,(0,start))
    closed = set()
    parent = dict()
    parent[start] = None
    best_g = dict()
    best_g[start] = 0

    while open:

        g,state = heapq.heappop(open)

        if g != best_g[state]:
            continue

        if state in closed:
            continue

        closed.add(state)

        if state == goal:
            path = list()
            x = state

            while x is not None:
                path.append(x)
                x = parent[x]

            path.reverse()

            return path,metrics("UCS",True,len(closed),len(path) - 1,g,t)

        for x in successors(grid,state):
            new_g = g + cost(grid[x[0]][x[1]])

            if x not in best_g or best_g[x] > new_g:
                best_g[x] = new_g
                parent[x] = state
                heapq.heappush(open,(new_g,x))

    return None,metrics("UCS",False,len(closed),0,None,t)

if __name__ == "__main__":

    grid = [
        [0,3,3,3,0],
        [0,0,0,0,0],
        [1,1,1,1,1]
    ]
    start = (0,0)
    goal = (0,4)

    path,m = ucs(grid,start,goal)
    show(path,m)