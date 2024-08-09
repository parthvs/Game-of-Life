import pygame
import random
width, height = 800, 600
grid_size = int(input("Enter individual cell size"))#individual cell size
pensize = int(input("enter pen size")) #your pen size when you click or draw



def initial_state(grid):
    i = len(grid)-1
    j = len(grid[0])-1
    no_of_cells = i*j
    for _ in range(int(no_of_cells/5)):
        x = random.randint(1,i)
        y = random.randint(1,j)
        grid[x][y] = 1
    return grid

def draw_grid(grid, grid_size):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                draw_cell(i, j, grid_size)

def draw_cell(i, j, grid_size):
    rect1 = pygame.Rect(i * grid_size, j * grid_size, grid_size, grid_size)
    pygame.draw.rect(screen, (255, 255, 255), rect1)

def update_grid(grid):
    new_grid = [row[:] for row in grid]
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            alive = (
                grid[i-1][j-1] + grid[i-1][j] + grid[i-1][j+1] +
                grid[i][j-1]                  + grid[i][j+1] +
                grid[i+1][j-1] + grid[i+1][j] + grid[i+1][j+1]
            )
            if grid[i][j] == 1:
                if alive < 2 or alive > 3:
                    new_grid[i][j] = 0
            else:
                if alive == 3:
                    new_grid[i][j] = 1
    return new_grid

def click(grid, x, y):
    x //= grid_size
    y //= grid_size
    if 0 <= x < len(grid)-pensize and 0 <= y < len(grid[0])-pensize:
        for i in range(pensize):
            for j in range(pensize):
                grid[x+i][y+j] = 1
    return grid


grid = [[0 for _ in range(height // grid_size)] for _ in range(width // grid_size)]
grid = initial_state(grid)
pygame.init()
screen = pygame.display.set_mode((width, height))
start = pygame.time.get_ticks()
dragging = False
clock = pygame.time.Clock()  # Used to manage frame rate
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                dragging = True
                x, y = event.pos
                grid = click(grid, x, y)
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Left mouse button
                dragging = False
        if event.type == pygame.MOUSEMOTION:
            if dragging:
                x, y = event.pos
                grid = click(grid, x, y)
    
    t = (pygame.time.get_ticks() - start) / 1000
    
    screen.fill((0, 0, 0))
     
    grid = update_grid(grid)
    draw_grid(grid, grid_size)
    pygame.display.flip()
    
    # Control the frame rate
    clock.tick(60)  # Limit 
    #pygame.time.wait(50)

pygame.quit()