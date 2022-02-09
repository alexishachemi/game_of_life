import sys
from time import sleep

g_size = 20
auto = False

grid = [[0 for i in range(g_size)] for i in range(g_size)]

def show_grid(grid=grid):
    for line in grid:

        print("\n", end="")
        for cell in line:
            sys.stdout.buffer.write(f"   {'■' if cell == 1 else '□'}  ".encode("utf-8"))
        print()

    print("\n\n")


def nearby_cells(cell_i, cell_j):
    nearby = []
    up = cell_i != 0
    down = cell_i != len(grid) - 1
    left = cell_j != 0
    right = cell_j != len(grid[cell_i]) - 1

    if up:
        nearby.append(grid[cell_i - 1][cell_j])
    
    if down:
        nearby.append(grid[cell_i + 1][cell_j])
    
    if left:
        nearby.append(grid[cell_i][cell_j - 1])
    
    if right:
        nearby.append(grid[cell_i][cell_j + 1])
    
    if up and left:
        nearby.append(grid[cell_i - 1][cell_j - 1])
    
    if up and right:
        nearby.append(grid[cell_i - 1][cell_j + 1])
    
    if down and left:
        nearby.append(grid[cell_i + 1][cell_j - 1])
 
    if down and right:
        nearby.append(grid[cell_i + 1][cell_j + 1])
    
    return nearby


def change_grid(grid1, grid2):
    for i, line in enumerate(grid2):
        for j, cell in enumerate(line):
            grid1[i][j] = cell


def update():
    global grid, auto
    temp_grid = [[0 for i in range(g_size)] for i in range(g_size)]
    
    change_grid(temp_grid, grid)
    
    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if cell == 0 and nearby_cells(i,j).count(1) == 3:
                temp_grid[i][j] = 1           
           
    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if cell == 1 and 2 <= nearby_cells(i,j).count(1) <= 3:
                temp_grid[i][j] = 1
    
    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if (cell == 1 and 2 <= nearby_cells(i,j).count(1) <= 3) == False and (cell == 0 and nearby_cells(i,j).count(1) == 3) == False:
                temp_grid[i][j] = 0
    
    if temp_grid == grid:
        auto = False
    
    change_grid(grid, temp_grid)
    

grid[10][9] = grid[10][10] = grid[11][10] = grid[9][10] = grid[9][11] = 1


show_grid()
user_input = input("enter X to stop, a for auto-scroll and anything else to continue: ").lower()
while not user_input in ["x","a"]:
    update()
    show_grid()
    user_input = input("enter X to stop, a for auto-scroll and anything else to continue: ").lower()

if user_input == "a":
    auto = True

while auto:
    try:
        sleep(0.3)
        update()
        show_grid()
        print("press ctrl+C to stop")
    
    except KeyboardInterrupt:
        auto = False
