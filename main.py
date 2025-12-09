import random
import pygame
import pdb

tile_sprite = 64

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

def texture_init():
    dico_texture = []
    # -- Snake head -- #
    snake_sprite = pygame.image.load("snake.png").convert()
    snake_sprite = pygame.transform.scale((snake_sprite), (tile_sprite, tile_sprite))
    dico_texture.append(snake_sprite)
    # -- Wall -- # 
    wall_sprite = pygame.image.load("wall.png").convert()
    wall_sprite = pygame.transform.scale(wall_sprite, (tile_sprite, tile_sprite))
    dico_texture.append(wall_sprite)
    return (dico_texture)

def display_map(grid):
    width = len(grid[0]) * tile_sprite
    height = len(grid) * tile_sprite

    pygame.init()
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    dico_texture = texture_init()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    # Mooving snake
                    print("moove")
        for i, row in enumerate(grid):
            for j, char in enumerate(row):
                if char == "1":
                    screen.blit(dico_texture[1], (j * tile_sprite, i * tile_sprite))
                elif char == "G":
                    screen.blit(dico_texture[0], (j * tile_sprite, i * tile_sprite))
        pygame.display.flip()
    pygame.quit()

    #for line in grid:
    #    print(line)

def main():
    print("Main")
    grid = generate_map(10, 10)
    display_map(grid)
    

if(__name__ == "__main__"):
    main()