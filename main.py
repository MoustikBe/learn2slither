import random
import pygame
import pdb

def generate_apple(grid, widht, height):
    #breakpoint()
    while(True):
        x_red = random.randint(1, height - 2)
        y_red = random.randint(1, widht - 2)
        if(grid[x_red][y_red] == "0"):
            grid[x_red][y_red] = "R"
            break
    while(True):
        x_green = random.randint(1, height - 2)
        y_green = random.randint(1, widht - 2)
        if(grid[x_green][y_green] == "0"):
            grid[x_green][y_green] = "G"
            break
    return(grid)

def generate_map(widht, height):
    #breakpoint()
    grid = []
    for i in range(height):
        row = []
        for j in range(widht):
            if(i == 0 or i == height - 1 or j == 0 or j == widht - 1):
                row.append("1")
            else:
                row.append("0")
        grid.append(row)
    return(generate_apple(grid, widht, height))

def display_map(grid):
    for line in grid:
        print(line)

def main():
    print("Main")
    grid = generate_map(10, 10)
    display_map(grid)
    

if(__name__ == "__main__"):
    main()