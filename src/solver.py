#---------------------------- TASK 1 ----------------------------
def count_neighbors(grid, row, col):
    """
    Counts the number of alive neighbors for a specific cell in the grid.
    A cell can have up to 8 neighbors (horizontal, vertical, and diagonal).
    
    Args:
        grid (list of lists): The current 2D state of the game.
        row (int): The row index of the cell.
        col (int): The column index of the cell.
        
    Returns:
        int: The total number of alive neighbors (0 to 8).
    """
    
    alive_count = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue  # skip the cell itself
            
            x, y = row + dx, col + dy

            if 0 <= x < rows and 0 <= y < cols: #For edge of the grid
                alive_count += grid[x][y] #Taking advantage of representing neighbour as 1
    return (alive_count)

#---------------------------- TASK 2 ----------------------------
def compute_next_generation(grid):
    """
    Generates the next state of the grid based on Conway's rules.
    
    Args:
        grid (list of lists): The current 2D state of the game.
        
    Returns:
        list of lists: A BRAND NEW 2D grid representing the next generation.
        
    Note:
        - Do NOT modify the original `grid` directly while iterating through it. 
          You must create a new grid to store the updated states, otherwise 
          your changes will mess up the neighbor counts for subsequent cells!
    """
    
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    
    # Create a new blank grid of the same size, filled with 0s (dead cells)
    next_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for x in range(rows):
        for y in range(cols):
            population = count_neighbors(grid, x, y)
            old_status = (grid[x])[y]
            if population > 3: #Overpopulation
                (next_grid[x])[y] = 0
            elif population < 2: #Underpopulation t
                (next_grid[x])[y] = 0
            elif 1< population < 4 and old_status == 1: #Survival
                (next_grid[x])[y] = 1
            elif (population == 3) and old_status == 0: #Repopulation
                (next_grid[x])[y] = 1
            
    return next_grid