# Warehouse Robot Simulator

A Python-based Warehouse Robot Simulator developed using **Pygame**. The project demonstrates and compares three pathfinding algorithms: Breadth-First Search (BFS), Uniform-Cost Search (UCS), and A* Search in a grid-based warehouse environment.

## Project Overview

The simulator represents a warehouse as a 2D grid containing free spaces, obstacles, and weighted terrain. A robot navigates from a starting position to a destination using a selected pathfinding algorithm.

The application provides a graphical interface to visualize the warehouse, display the selected path, animate robot movement, and compare algorithm performance.

## Features

- Three pathfinding algorithms: BFS, UCS, and A*.
- Three predefined warehouse layouts: Easy, Medium, and Hard.
- Grid-based warehouse environment.
- Obstacle and weighted-terrain representation.
- Visual path display and robot animation.
- Algorithm selection through keyboard controls.
- Performance dashboard displaying:
  - Execution time
  - Explored nodes
  - Path length
  - Total path cost
  - Search success status

## Technologies Used

- **Programming Language:** Python
- **GUI Framework:** Pygame
- **Algorithms:** BFS, Uniform-Cost Search, A*
- **Development Environment:** Visual Studio Code

## Project Structure

```text
Warehouse-Robot-Simulator/
│
├── project_backup.py    # Main application and GUI
├── warehouse.py         # Warehouse environment and layouts
├── bfs.py               # Breadth-First Search
├── ucs.py               # Uniform-Cost Search
├── astar.py             # A* Search
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Navigate to the project folder

```bash
cd Warehouse-Robot-Simulator
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Install dependencies

**Windows:**
```powershell
.\venv\Scripts\python.exe -m pip install -r requirements.txt
```

**Linux / macOS:**
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### 5. Run the application

```bash
python project_backup.py
```

The application window will open and display the warehouse simulator.

## Keyboard Controls

| Key | Action |
|---|---|
| Q | Select Board 1 – Easy |
| W | Select Board 2 – Medium |
| E | Select Board 3 – Hard |
| 1 | Run Breadth-First Search (BFS) |
| 2 | Run Uniform-Cost Search (UCS) |
| 3 | Run A* Search |

## Algorithms Implemented

### 1. Breadth-First Search (BFS)
Explores nodes level by level using a FIFO queue. It finds a path with the minimum number of moves when all moves have equal cost.

### 2. Uniform-Cost Search (UCS)
Expands the node with the lowest accumulated path cost using a priority queue. It considers weighted terrain while finding a minimum-cost path.

### 3. A* Search
Combines the accumulated path cost and a heuristic estimate to guide the search.

The project uses **Manhattan Distance** as its heuristic:

`f(n) = g(n) + h(n)`

## Performance Evaluation

The simulator compares the algorithms using the following parameters:

- Execution time
- Number of explored nodes
- Path length
- Total path cost

These measurements help visualize differences in the search strategies and their performance on warehouse layouts.

## Team Members and Contributions

| Member | Name | Roll Number | Contribution |
|---|---|---|---|
| Member 1 | Dhanush Samudrala | CS25B2044 | Warehouse Environment & Problem Formulation |
| Member 2 | Punit Raghvendra | CS25B2043 | BFS & Uniform-Cost Search |
| Member 3 | D. Kishore Krishna | CS25B2010 | A* Search & Heuristic Optimization |
| Member 4 | V. Pavan Sai | CS25B2025 | User Interface & System Integration |

## Future Enhancements

- Interactive warehouse map creation.
- Dynamic obstacle handling and route replanning.
- More warehouse layouts and test scenarios.
- Enhanced performance visualization.
- Integration with physical mobile robots.

## Dependencies

The project requires Python 3.x and Pygame.

Install dependencies using:

```bash
pip install -r requirements.txt
```

## Acknowledgement

This project was developed as part of the Artificial Intelligence with Python coursework at the Indian Institute of Information Technology, Design and Manufacturing, Kancheepuram.

---

**Warehouse Robot Simulator – Intelligent Pathfinding and Navigation Visualization.**
