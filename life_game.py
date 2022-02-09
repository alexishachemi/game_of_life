import sys

g_size = 10

grid = [[0 for i in range(g_size)] for i in range(g_size)]

def show_grid(grid=grid):
    for line in grid:
        [print(" -----", end="") for i in range(g_size)]
        print("\n|", end="")
        for cell in line:
            sys.stdout.buffer.write(f"  {'■' if cell == 1 else '□'}  |".encode("utf-8"))
        print()
    [print(" -----", end="") for i in range(g_size)]
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
    global grid
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
    
    change_grid(grid, temp_grid)
    

grid[5][5]  = grid[5][6] = grid[5][4] = 1
grid[6][5] = 1

show_grid()
while input("enter X to stop and anything else to continue: ").lower() != "x":
    update()
    show_grid()