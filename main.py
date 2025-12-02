import random
import pygame

# adding point #
green_apple = 0
# removing point #
red_apple = 0


map_example = [
    ["1", "1", "1", "1", "1", "1"],
    ["1", "0", "0", "0", "0", "1"],
    ["1", "0", "0", "0", "0", "1"],
    ["1", "0", "0", "0", "0", "1"],
    ["1", "0", "0", "0", "0", "1"],
    ["1", "0", "0", "0", "0", "1"],
    ["1", "0", "0", "0", "0", "1"],
    ["1", "1", "1", "1", "1", "1"]
]

def main():
    print("Main")

    for i in range(2):
        if(i == 1):
            letter = 'R'
        else:
            letter = 'G'
        line = random.uniform(1, 7)
        box = random.uniform(1, 4)
        map_example[int(line)][int(box)] = letter

    for line in map_example:
        print("-> ", line)

if(__name__ == "__main__"):
    main()