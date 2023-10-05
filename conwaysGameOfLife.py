#    Rules

#    Any live cell with fewer than two live neighbours dies, as if by underpopulation.

#    Any live cell with two or three live neighbours lives on to the next generation.

#    Any live cell with more than three live neighbours dies, as if by overpopulation.

#    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

import curses
import random
import time

def create_grid(width, height):
    return [[random.choice([0, 1]) for _ in range(width)] for _ in range(height)] #random 1,0 fill for the grid

def update_grid(grid):

    #some terminal won't work without this
    #gets anew grid with all 0s
    new_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            #iterate 3x3 around origin i,j
            #   x x x
            #   x C x
            #   x x x
            neighbors = [
                grid[x][y]
                for x in range(i - 1, i + 2)
                for y in range(j - 1, j + 2)
                if 0 <= x < len(grid) and 0 <= y < len(grid[i]) and (x != i or y != j)
            ]
            live_neighbors = sum(neighbors)

            #determine the next state
            if grid[i][j] == 1:
                if live_neighbors in [2, 3]:
                    new_grid[i][j] = 1
            elif grid[i][j] == 0:
                if live_neighbors == 3:
                    new_grid[i][j] = 1

    return new_grid

def draw_grid(stdscr, grid, height, width):
    try:
        for i in range(min(len(grid), height)):
            for j in range(min(len(grid[i]), width)):
                if grid[i][j] == 1:
                    stdscr.addch(i, j, ord("@"))#alive
                else:
                    stdscr.addch(i, j, ord(" "))#dead
    except curses.error:
        print(curses.error)


def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(1)

    height, width = stdscr.getmaxyx()# Get terminal dimensions
    grid = create_grid(width, height)

    while True:
        stdscr.clear()
        grid = update_grid(grid, )
        draw_grid(stdscr, grid, height, width)
        stdscr.refresh()
        time.sleep(0.1)  # Adjust the speed here

        # Wait for a key press or quit when 'q' is pressed
        key = stdscr.getch()
        if key == ord('q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)
