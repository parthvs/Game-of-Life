# Conway's Game of Life

This project is an implementation of Conway's Game of Life using Python and Pygame.

## Description

Conway's Game of Life is a cellular automaton simulation where cells on a grid evolve over time according to a set of rules. This implementation allows users to interact with the simulation by drawing live cells and watching the evolution of the system.
The rules are:
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
## Features

- Customizable grid size and pen size
- Click and drag to draw live cells
- Random initial state generation
- Real-time simulation updates

## Requirements

- Python 3
- Pygame

## Installation

1. Ensure you have Python installed on your system.
2. Install Pygame by running:
pip install pygame
3. Clone this repository:  
`git clone https://github.com/parthvs/Game-of-Life.git`
`cd Game-of-Life`

## Usage

Run the script using Python:
`python CGOL.py`   
When prompted:
1. Enter the desired cell size
2. Enter the desired pen size

Use your mouse to draw live cells on the grid. The simulation will start automatically.

## Controls

- Left-click and drag to draw live cells
- Close the window to exit the simulation



## Acknowledgements

This project is based on Conway's Game of Life, developed by mathematician John Conway in 1970.
