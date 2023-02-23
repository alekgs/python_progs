board = [[' ' for _ in range(3)] for _ in range(3)]
players = ['X', 'O']


def print_board():
    for row in board:
        print('|'.join(row))


def get_move(player):
    while True:
        try:
            row = int(input(f"{player}, enter row (0-2): "))
            col = int(input(f"{player}, enter col (0-2): "))
            if row in [0, 1, 2] and col in [0, 1, 2] and board[row][col] == ' ':
                board[row][col] = player
                return
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Invalid input, try again.")


def check_win():
    # check rows
    for row in board:
        if row[0] != ' ' and row[0] == row[1] == row[2]:
            return row[0]
    # check columns
    for col in range(3):
        if board[0][col] != ' ' and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]
    # check diagonals
    if board[0][0] != ' ' and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] != ' ' and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return None


def play_game():
    for i in range(9):
        player = players[i % 2]
        print_board()
        get_move(player)
        winner = check_win()
        if winner:
            print(f"{winner} wins!")
            return
    print("It's a tie!")


play_game()
