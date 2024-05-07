board = '|1|2|3|\n|4|5|6|\n|7|8|9|'
cells = 9

def print_board():
    print(board)
#########################################################################
def check_winner(symbol):
    lines = [board[1:6], board[8:14], board[15:22],         # 1-3,4-6,7-9
            board[1:22:8], board[3:20:8], board[5:22:8],    # 1-4-7, 2-5-8, 3-6-9
            board[1:22:10], board[5:22:6]                   # 1-5-9, 3-5-7
]           
    for line in lines:
        if line.count(symbol) == 3:
            return True
    return False

print_board()
#########################################################################
while cells > 0:
    while True:
        player_1 = input('Player 1: Please enter a number (1-9): ')

        if player_1.isdigit() and 1 <= int(player_1) <= 9:
            position = int(player_1)

            if board.count(str(position)) == 1:
                board = board.replace(str(position), 'X')
                cells -= 1
                print_board()
                if check_winner('X'):
                    print("Player 1 wins!")
                    cells = 0
                break
            else:
                print('This position is taken, try again: ')
        else:
            print('Invalid input! Please enter a number between 1 and 9.')

    if cells == 0 and not check_winner('X'):
        print("Draw!")
        break
    if cells == 0:
        break
#########################################################################
    while True:
        player_2 = input('Player 2: Please enter a number (1-9): ')

        if player_2.isdigit() and 1 <= int(player_2) <= 9:
            position = int(player_2)

            if board.count(str(position)) == 1:
                board = board.replace(str(position), 'O')
                cells -= 1
                print_board()
                if check_winner('O'):
                    print("Player 2 wins!")
                    cells = 0
                break

            else:
                print('This position is taken, try again: ')

        else:
            print('Invalid input! Please enter a number between 1 and 9.')

    if cells == 0 and not check_winner('O'):
        print("Draw!")
        break
    if cells == 0:
        break