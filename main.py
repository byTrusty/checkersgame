from checkers import *

def game():
    size = int(input("Enter board size (between 4 and 16): "))
    board = build_board(size)
    print(board)
    print("Empty cells:", get_count(board, 'Empty'))
    print("Red checkers:", get_count(board, 'Red'))
    print("Black checkers:", get_count(board, 'Black'))

if __name__ == '__main__':
    game()


#yay
