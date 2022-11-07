"""
    Motivation:
        I want to make a robovac
        imagine your room is a grid 2d list where it's a rectangular room
        
        search for a special point on the floor.
            totally blind, just like eufy
            
        * walls
        S = starting location
        I = item we want to find

"""

import random

WALL = '*'
SPACE = ' '
THE_ANSWER = 'A'

def make_random_grid(rows, cols, p=0.2):
    the_grid = [[WALL if random.random() < 0.2 else SPACE for j in range(cols)] for i in range(rows)]
    the_grid[random.randint(0, rows - 1)][random.randint(0, cols - 1)] = THE_ANSWER
    return the_grid

def display_grid(the_grid):
    for i in range(len(the_grid)):
        for j in range(len(the_grid[i])):
            print(the_grid[i][j], end='\t')
        print()


def pathfind(the_grid, pos_x, pos_y, visited):
    # these are the recursive base cases
    if the_grid[pos_x][pos_y] == THE_ANSWER:
        return [(pos_x, pos_y)]
    if (pos_x, pos_y) in visited:
        # if we make a loop, end up in the same place again
        # this path didn't get to the answer.
        return []
    
    # keeping track of all the places we've been
    # if you've searched a place before then it doesn't lead to
    #   the answer
    visited.append((pos_x, pos_y))
    # print((pos_x, pos_y))
    # up
    if pos_x > 0 and the_grid[pos_x - 1][pos_y] != WALL:  # at least one, minus one is greater than or equal to zero
        path = pathfind(the_grid, pos_x - 1, pos_y, visited)
        if path:  # if its not empty, it gets to the answer
            path.append((pos_x, pos_y))
            return path
    # right
    if pos_y < len(the_grid[pos_x]) - 1 and the_grid[pos_x][pos_y + 1] != WALL:
        path = pathfind(the_grid, pos_x, pos_y + 1, visited)
        if path:  # if its not empty, it gets to the answer
            path.append((pos_x, pos_y))
            return path
    # down
    if pos_x < len(the_grid) - 1 and the_grid[pos_x + 1][pos_y] != WALL:
        path = pathfind(the_grid, pos_x + 1, pos_y, visited)
        if path:  # if its not empty, it gets to the answer
            path.append((pos_x, pos_y))
            return path
    # left
    if pos_y > 0 and the_grid[pos_x][pos_y - 1] != WALL:
        path = pathfind(the_grid, pos_x, pos_y - 1, visited)
        if path:  # if its not empty, it gets to the answer
            path.append((pos_x, pos_y))
            return path
    
    return []


the_grid = make_random_grid(10, 10, 0.35)
display_grid(the_grid)
the_visited_list = []
the_path = pathfind(the_grid, 0, 0, the_visited_list)
the_path.reverse()
print(the_path)

step = 0
for x, y in the_path:
    if the_grid[x][y] != THE_ANSWER:
        the_grid[x][y] = str(step)
    step += 1
display_grid(the_grid)

"""
    Calculation time vs optimal path
    
    DFS = depth first search much faster in calculation time
        = very bad paths in general, usually super long
    BFS = breadth first search - searches every path of length n
        before it searches any paths of length n + 1
        more computation in general, more places visited
        has to return the best path
"""
