"""
    While loops
    
        for loops
            for - i loop which loops over indices = range(1, 10, 2) for example
                    range(len(some_list))
            for each loop - loops over elements.
        
        when you know the number of times you need to run a loop

    A while loop is used when you need to run until a condition is True/False
    
    while <condition>:
        your code in here
    
    A while loop is an if statement on repeat
    
"""
if False:
    the_list = [1, 4, 7, 9, 12]
    
    # in a for each loop, the x is actually a 'copy' of the element in the list
    for x in the_list:
        print(x)
        # x = 3 doesn't modify the list itself only the temp value
    print()
    
    for i in range(len(the_list)):
        print(the_list[i])
        # if you need to assign into the list, use this one
        the_list[i] = i ** 2
    
    print(the_list)
    """
        When the loop condition is false before you enter the first time
        I call this a "skipped loop"
            for i in range(10, -2, 5):
                print(i)
                
        Whenever the while condition is True never changes -->
            infinite loop
        
        
    """
    value = int(input('Enter a number: '))
    while value < 0:
        print('X was negative, enter a positive value')
        value = int(input('Enter a number: '))
        
    print('The square root of value is ', value ** (1/2))
    
    count = 0
    # this loop is calculating "discrete log of value"
    while value > 1:
        value //= 2
        # value = value // 2
        count += 1
        
    print('The loop ran', count, 'times')
    
    secret_password = 'secret1234'
    usr_password = input('Tell me password: ')
    attempts = 1
    while usr_password != secret_password and attempts < 3:
        usr_password = input('That was not correct, tell me password! ')
        attempts += 1
    
    if usr_password == secret_password:
        print('LOGGED IN!')
    else:
        print('NOT LOGGED IN TOO MANY ATTEMPTS')
        

"""
    Games... = easy project generators

    Hypothetically tic tac toe - we don't know how many turns
        until victory, so while loop
"""
# flag variables
horizontal_line = False
vertical_line = False
diagonal_line = False

the_board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]

turn = 0

def get_move(the_board):
    # code in here
    pass


while not horizontal_line and not vertical_line and not diagonal_line:
    for i in range(len(the_board)):
        for j in range(len(the_board) - 1):
            print(the_board[i][j], end='|')
        print(the_board[i][len(the_board[i]) - 1], end='\n')
        if i < len(the_board) - 1:
            print('-----')
    
    if turn % 2 == 0:
        print('it is xs turn')
        """
            1) input the user's position "3 2"
            2) split the numbers
            3) cast them to integers
            4) make sure they're in range
            5) if not go back to step 1
        """
        valid_move = False
        while not valid_move:
            move = input('Tell me your move in this format x y: ')  # 3 2
            split_move = move.split()
            if len(split_move) == 2:
                x = int(split_move[0])
                y = int(split_move[1])
                
                if 1 <= x <= 3 and 1 <= y <= 3 and the_board[x - 1][y - 1] == ' ':
                    valid_move = True
        the_board[x - 1][y - 1] = 'x'
    else:
        valid_move = False
        while not valid_move:
            move = input('Tell me your move in this format x y: ')  # 3 2
            split_move = move.split()
            if len(split_move) == 2:
                x = int(split_move[0])
                y = int(split_move[1])
            
                if 1 <= x <= 3 and 1 <= y <= 3 and the_board[x - 1][y - 1] == ' ':
                    valid_move = True
        the_board[x - 1][y - 1] = 'o'
    
    """
        Detect row victories
    """
    for row in the_board:
        if row[0] == row[1] == row[2] and \
            (row[0] == 'x' or row[0] == 'o'):
            horizontal_line = True
            winner = row[0]
    """
        Detect Col victories
    """
    for col in range(len(the_board)):
        current = the_board[0][col]
        found = True
        for row in range(len(the_board)):
            if current != the_board[row][col]:
                found = False
        if found and current == 'x':
            vertical_line = True
            winner = 'x'
        elif found and current == 'o':
            vertical_line = True
            winner = 'o'
    """
        Detect diagonal victories
    """
    
    """
        Detect anti-diagonal victories
    """
    
    turn += 1
    
