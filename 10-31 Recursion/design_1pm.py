"""
    Let's talk about functions again.

    How do we decide to make a function?
        Maybe you notice that this bit of code is somewhat
            independent from the rest of the code.
        The code segment is repeated in various places in your
            program.
    What should it do?

"""

"""
If you were going to write a chess program
    Players move the pieces,
        are we allowed to move this piece to that position?
        move the piece on the board
        check to see if there was a capture.
    Is the game over?
        check positions
        checkmate positions
"""


def check_mate(board):
    pass


"""
    determine whether or not a specific move is allowed
    1) what is a good name for this function?
        can_move, moveable, is_movable, legal_move
    2) what does this function need to be able to do its job?
        add arguments for whatever the function needs to do
        in the legal_move case: needs the board, start, end, current turn
        those become your parameters
    3) what should the function return?
        what kind of type should the function return?
            boolean as type
        what does that variable mean?
            if you can move, then True, else False

"""
"""
    look at the board,
        1) make sure the piece exists
        2) make sure it's your piece that you can move
        3) make sure the destination is allowed

    You might call this "top-down design"
"""


def legal_move(the_board, starting_pos, ending_pos, current_turn):
    """
    :param the_board: two dimensional list which represents the current board state
    :param starting_pos: list with [x, y] coordinate
    :param ending_pos: list with [x, y] coordinate
    :param current_turn: int, current turn, even = white, black = odd
    :return: boolean, whether the move is legal
    """
    pass


def check_mate(the_board, turn):
    """
    :param the_board: 2d-list with the board data
    :param turn: int, turn count; maybe we need this
    :return: 'B', 'W' whoever is in checkmate or '' for none
    """
    pass


def run_game():
    board = []  # i should make a function that sets up a chessboard
    captures = []
    turn = 0
    while not check_mate(board):
        # move the pieces
        input('What is your move? ')
        starting_move, ending_move = 0, 0
        if legal_move(board, starting_move, ending_move, turn):
            pass
        else:
            print('That is not a legal move.')
        # DO NOT DELETE ME
        turn += 1
