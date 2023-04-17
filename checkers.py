from numpy import random, count_nonzero, resize, transpose

def build_board(size):
    choices = ['Empty', 'Red', 'Black']
    board = random.choice(choices, size=(size, size))
    return board

def get_count(board, item):
    return count_nonzero(board == item)

def resize_board(board, new_size):
    return resize(board, (new_size, new_size))

def pivot_board(board):
    return transpose(board)

if __name__ == '__main__':
    print("This file is not intended to be run as a main.")
