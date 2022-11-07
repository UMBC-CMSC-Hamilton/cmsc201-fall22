import random

WALL = '*'
SPACE = '_'
THE_ANSWER = 'A'


def build_grid(rows, cols, p=0.3):
    # list comprehension == laziness of the professor
    # return [['*' if random.random() < p else ' ' for _ in range(cols)] for _ in range(rows)]
    the_grid = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            if random.random() <= p:
                new_row.append(WALL)
            else:
                new_row.append(SPACE)
        the_grid.append(new_row)
    the_grid[0][0] = SPACE
    the_grid[random.randint(0, rows - 1)][random.randint(0, cols - 1)] = THE_ANSWER
    return the_grid


def display_board(the_grid):
    for row in the_grid:
        for j in range(len(row)):
            print(row[j], end='\t')
        print()


def pathfinder(the_grid, pos_x, pos_y, visited):
    """
        we need a base case... how do we know when to stop?
            try all paths and doesn't work
            find the 'A'
            what if the current position is visited already?
    """
    if the_grid[pos_x][pos_y] == THE_ANSWER:
        return [(pos_x, pos_y)]
    if (pos_x, pos_y) in visited:
        return []
    
    # tuples are immutable lists
    visited.append((pos_x, pos_y))
    
    # up
    if pos_x > 0 and the_grid[pos_x - 1][pos_y] != WALL:
        path = pathfinder(the_grid, pos_x - 1, pos_y, visited)
        if path:
            path.append((pos_x, pos_y))
            return path
        # if it finds a path we want to add the current position
        # to the path and then return that path.
        # what will get returned is... a path = list of tuples
    # right
    if pos_y < len(the_grid[pos_x]) - 1 and the_grid[pos_x][pos_y + 1] != WALL:
        path = pathfinder(the_grid, pos_x, pos_y + 1, visited)
        if path:
            path.append((pos_x, pos_y))
            return path
    # down
    if pos_x < len(the_grid) - 1 and the_grid[pos_x + 1][pos_y] != WALL:
        path = pathfinder(the_grid, pos_x + 1, pos_y, visited)
        if path:
            path.append((pos_x, pos_y))
            return path
    # left
    if pos_y > 0 and the_grid[pos_x][pos_y - 1] != WALL:
        path = pathfinder(the_grid, pos_x, pos_y - 1, visited)
        if path:
            path.append((pos_x, pos_y))
            return path
    
    return []

"""
    DFS = Depth First Search
        is there a way to find a better path?
            yes
    Balance between computation time and path length.
    
    BFS = Breadth First Search
        finds the best path
        searches ALL positions that are that distance
        bit more calculation time
"""


my_grid = build_grid(7, 7)
display_board(my_grid)
visited = []
the_answer = pathfinder(my_grid, 0, 0, visited)
the_answer.reverse()
count = 0
for x, y in the_answer:
    my_grid[x][y] = str(count)
    count += 1

for x, y in visited:
    if my_grid[x][y] == SPACE:
        my_grid[x][y] = 'V'
print('Answer with path:')
display_board(my_grid)

