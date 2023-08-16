#------ Ahmed_Osama_Elkhadrawi--------#

#  Create a function to print the game board to the console.

def print_game_board(board):
    for row in board:
        print("|".join(row))
        print("-" *5)

#  Create a function to handle player moves. 

def handle_move(board, player):
    while True:
        row = int(input('Enter the row (0-2): '))
        col = int(input('Enter the column (0-2): '))
        if board[row][col] == '':
            board[row][col] = player
            break
        else:
            print('Try again..this square is taken')

# Create a function to check for a win. and check if any of the rows, columns, or diagonals of the board contain three of the player's symbols in a row

def check_win(board, player):
    # Checking_rows
    for row in board:
        if all(square == player for square in row):
            return True

    # Checking_columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False
#  check if every square on the board has been filled

def check_Tie(board):
    for row in board:
            if '' in row:
                return False
    return True        

# 
def play_game():

    board = [['', '', ''], ['', '', ''], ['', '', '']]
    players = ['X', 'O']
    current_player = 0

    while True:
        print_game_board(board)
        player = players[current_player]
        print(f"Player's turn=>> {player} ")
        handle_move(board, player)

        if check_win(board, player):
            print_game_board(board)
            print("Player {} wins".format(player))
            break
        elif check_Tie(board):
            print_game_board(board)
            print("tie try again")
            break

        current_player = (current_player + 1) % 2

# Starting the game

play_game()
