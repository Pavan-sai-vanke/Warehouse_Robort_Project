
# Import warehouse environment
from warehouse import create_warehouse, validate_warehouse

# Import all three search algorithms
from bfs import bfs
from ucs import ucs
from astar import astar


# Get warehouse grid, start and goal
grid, start, goal = create_warehouse()

# Validate the warehouse
validate_warehouse(grid, start, goal)

# Store algorithms for testing
algorithms = [ 
    ("BFS", bfs),
    ("UCS", ucs),
    ("A*", astar)
]

print("=" * 50)
print("WAREHOUSE ROBOT - INTEGRATION TEST")
print("=" * 50)

print("\nWarehouse:")
for row in grid:
    print(row)

print("\nStart:", start)
print("Goal:", goal)

# Test each algorithm
for name, algorithm in algorithms:

    print("\n" + "=" * 50)
    print(name, "RESULT")
    print("=" * 50)

    path, metrics = algorithm(grid, start, goal)

    print("Path:", path)

    for key, value in metrics.items():
        print(key, ":", value)

    # Verify common output format
    required_keys = {
        "algorithm",
        "success",
        "execution_time",
        "explored_nodes",
        "path_length",
        "path_cost"
    }

    assert isinstance(metrics, dict)
    assert required_keys.issubset(metrics.keys())
    assert metrics["success"] == (path is not None) 

print("\nALL INTEGRATION TESTS COMPLETED!")
