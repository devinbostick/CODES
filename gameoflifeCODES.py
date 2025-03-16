import turtle
import time

# Screen setup
turtle.setup(600, 600)
turtle.bgcolor("black")
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0, 0)

# Grid size and cell size
grid_size = 50
cell_size = 10

# Helper function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Initialize grid with prime-driven cells (only at prime-numbered positions)
def create_grid():
    grid = []
    for y in range(grid_size):
        row = []
        for x in range(grid_size):
            # Place a live cell at prime-numbered x, y positions
            if is_prime(x) and is_prime(y):
                row.append(1)  # Cell is alive
            else:
                row.append(0)  # Cell is dead
        grid.append(row)
    return grid

# Draw grid based on current state
def draw_grid(grid):
    turtle.clear()
    for y in range(grid_size):
        for x in range(grid_size):
            if grid[y][x] == 1:
                turtle.penup()
                turtle.goto(x * cell_size - 250, 250 - y * cell_size)
                turtle.pendown()
                turtle.color("yellow")
                turtle.begin_fill()
                turtle.circle(cell_size / 2)
                turtle.end_fill()

# Count alive neighbors of a cell, with prime-driven birth/death conditions
def count_neighbors(grid, x, y):
    neighbors = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            nx, ny = x + i, y + j
            if 0 <= nx < grid_size and 0 <= ny < grid_size:
                neighbors += grid[ny][nx]
    return neighbors

# Update the grid with prime-driven birth and death
def update_grid(grid):
    new_grid = [[0] * grid_size for _ in range(grid_size)]
    for y in range(grid_size):
        for x in range(grid_size):
            neighbors = count_neighbors(grid, x, y)
            
            # Chirality: Cells with prime neighbors follow unique rules
            prime_factor = 1 if is_prime(neighbors) else 0

            # Prime resonance effect: Cells with prime neighbors follow a different pattern
            if grid[y][x] == 1 and (neighbors == 2 or neighbors == 3 or prime_factor == 1):
                new_grid[y][x] = 1  # Cell survives or stays alive
            elif grid[y][x] == 0 and neighbors == 3:
                new_grid[y][x] = 1  # New cell born
            elif grid[y][x] == 0 and prime_factor == 1:
                new_grid[y][x] = 1  # New cell born due to resonance-based rule

    return new_grid

# Main function to run the game
def main():
    grid = create_grid()
    while True:
        draw_grid(grid)
        grid = update_grid(grid)
        turtle.update()
        time.sleep(0.1)

turtle.Screen().title("CODES-Prime Resonance Game of Life")
main()