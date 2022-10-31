"""
    Design of programs/functions
        
        Top down design - design the main functionaltiy first,
            then you design the smaller and smaller functionality
                later
    
    Example: minesweeper
        
        What parts do you need?
            the_grid <- 2d list with nothing or mine
        
        display the grid
            calculate the number of adjacent mines
        
        user enter a position
        check if it's a mine or not
        if it is -> game over
        if not -> reveal more grid
        
        user has to be able to mark a mine
        
        -> Tells you what functions you need
"""

"""
    How do you decide on what functions should be?
        You have a piece of code which is somewhat independent
            from other parts of your program.
        Prevent you from repeating code
"""

"""
    0) Decide you want a function that makes the grid.
    1) Decide a name for your function.
        create_grid, make_grid, fill_new_grid, make_minesweeper
    2) Decide on parameters:
        Think what does this function need in order to do its job?
        need to know the dimensions of the grid.
        need to know the number of mines.
    3) Think about if you need a return.
        Does the function create something you want to give back
            to the rest of your program?
                Yes, it makes my grid, i want to return something
            The rest of the program needs the grid, i must return it.
"""

from random import random, randint


def make_minesweeper_grid(rows, cols, num_mines):
    """
    :param rows: int, number of rows
    :param cols: int, number of cols
    :param num_mines: int, number of mines, should be less than
                    rows * cols
    :return:
    """
    current_mines = 0
    minesweeper_grid = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            # slightly hard implementation
            # random() returns a float between 0 and 1
            if random() <= num_mines / (rows * cols) and current_mines < num_mines:
                new_row.append('*')
                current_mines += 1
            else:
                new_row.append(' ')
        minesweeper_grid.append(new_row)
    
    while current_mines < num_mines:
        x = randint(0, rows)
        y = randint(0, cols)
        if minesweeper_grid[x][y] != '*':
            minesweeper_grid[x][y] = '*'
            current_mines += 1
    
    return minesweeper_grid


def game_over():
    return True

"""
    1) we want to display the minesweeper grid, so I say, display_grid
    2) we need the information of whether the person has already
        made that square visible
        two parameters two lists one is the actual grid
        second parameter is going to be some other 2d-list we
            haven't made yet
    3) does display need to return anything?
        no probably not, why not? it should be an advanced form
        of print
"""
def display_grid(minesweeper_grid, visible_grid):
    pass


"""
    get user input function
    0) we want to make sure the user enters a valid input
    1) decide on a name
        get_valid_position, get_user_input, get_user_click
    2) what are the parameters? it needs the grid, nothing else
        just minesweeper_grid
    3) what should it return? what does the function give back?
        4, 7
        split the thing, cast them to integers, stick them in a
            list.
        return the list of two elements
"""

def get_valid_position(minesweeper_grid):
    """
    :param minesweeper_grid: 2d list of '*' = mines, or spaces
    :return: a list with two elements, which is the valid position
    """
    
    pos = [1, 2]
    return pos

def check_mine(user_pos, the_grid):
    """
    :param user_pos:
    :param the_grid:
    :return:
    """
    x = user_pos[0]
    y = user_pos[1]
    if the_grid[x][y] == '*':
        return True
    else:
        return False


def reveal_board(the_grid, visible_info):
    pass


def run_game(x, y, mines):
    #
    the_grid = make_minesweeper_grid(x, y, mines)
    visible_info = []

    game_over = False
    while not game_over:
        # user will pick a position
        # either click on it, mark as mine
        user_pos = get_valid_position(the_grid)
        # check if it's a mine
        game_over = check_mine(user_pos, the_grid)
        # if not, reveal more of the board
        reveal_board(the_grid, visible_info)
        display_grid(the_grid, visible_info)
        
