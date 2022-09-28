"""
2d lists, nested for loops and while loops

*
**
***
****
*****
"""
if False:
    height = int(input('enter the height: '))
    for i in range(height):
        for j in range(i + 1):
            print("*", end='')  # no newline here
        print()  # this will give me the newline
    
    """
        What if i wanted to draw an upside down triangle?
        
    """
    
    for i in range(height):
        for j in range(height - i):
            print("*", end='')
        print()
        
    print('\n\n')
    
    
    for i in range(height, 0, -1):
        for j in range(i):
            print("*", end='')
        print()
    
    """
        sum up the anti-diagonal of a square 2d list
        
        2d_list = rows x cols
        
        
    """
    
    square_list = [
        [0, 4, 2, 8],
        [1, 5, 9, 7],
        [2, 8, 13, 5],
        [4, 5, 6, 7]
    ]
    
    # square_list[2] second row
    # square_list[2][3] second row third col.
    
    """
    Ex. Scan over and add up the "anti-diagonal"
        in this case 8, 9, 8, 4
    """
    total = 0
    for i in range(len(square_list)):
        print(square_list[i][len(square_list) - i - 1])
        total += square_list[i][len(square_list) - i - 1]
    
    
    """
        While loops
            what are while loops?
                what makes them different from for loops?
    
        for each loop, scans over the elements of a list
        for i loop which scans over the indices or some range
        
            the number of times that a for loop runs is "fixed"
                at the start of the loop
        
        While loop runs as long as a "condition" is true
        If statements if you turn on repeat
        
        
        If the condition is false the first time, I call that a
            'skipped loop'= initial condition was false, never ran
    """
    
    x = -4
    while x >= 0:
        x = int(input(f'You entered {x} tell me a new x: '))
    
    print('You entered a negative x', x)
    
    """
        Infinite loop = a loop that runs infinitely
            never hits a terminating condition, etc
    # """
    # x = 0
    # while x >= 0:
    #     x += 1
    #     print(x)
    
    
    x = int(input('Enter new x: '))
    while x >= 0:
        # 20 lines of code in here
        print(x)
        # you will forget to do this:
        x = x - 1  # x -= 1
        
    
    my_password = 'secret1234'
    password = input('Tell me password: ')
    while password != my_password:
        print('Your password was incorrect, retry.')
        # make sure that you modify password inside the loop
        password = input('Tell me password: ')
    
    
    x = int(input('Enter a positive number: '))
    while x <= 0:
        x = int(input('That was not positive, enter a positive number: '))
    
    # you can make a while loop that emulates a for loop
    # emulate range(1, 10, 2)
    print('For loop:')
    for i in range(1, 10, 2):
        print(i)
    
    print('While loop:')
    index = 1
    while index < 10:
        print(index)
        index += 2

"""
    Every for loop can be remade into a while loop
    
    can every while loop be made into a for loop? no
"""

"""
    Uses of a while loop:
        user input - make sure user enters correct data
        run program until you receive a quit message/
            GUI = graphical user interface (UI)
                UX = terrible [user experience]
        while game is running
"""
the_board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']
             ]
completed_row = False
completed_col = False
completed_diag = False
turn = 0
while not completed_row and not completed_col and not completed_diag:
    for i in range(len(the_board)):
        for j in range(len(the_board[i])):
            print(the_board[i][j], end='|')
        print('\n---------')
        
    if turn % 2 == 0:
        # User going to enter 1 3
        move = input('Tell me your move: ')
        valid_move = False
        while not valid_move:
            split_move = move.split()
            if len(split_move) == 2:
                x = int(split_move[0])
                y = int(split_move[1])
                if 1 <= x <= 3 and 1 <= y <= 3:
                    valid_move = True
                else:
                    print('Invalid move choice.  ')
            
            if not valid_move:
                move = input('Tell me your move: ')

        print(x, y)
        the_board[x - 1][y - 1] = 'x'

    elif turn % 2 == 1:
        pass  # o's turn
    # input('Stop please')
    turn += 1