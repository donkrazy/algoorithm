import copy


def print_help(board):
    print('===========result===========')
    for row in board:
        print(row)


def put_block(board):
    flag = True
    height = len(board)
    width = len(board[0])

    for i in range(height):
        for j in range(width):
            if board[i][j] != '.':
                continue
            if j == width - 1:
                continue
            if i == height - 1:
                continue
            if board[i][j + 1] == '.' and board[i + 1][j] == '.':
                flag = False
                board_copy = copy.deepcopy(board)
                board_copy[i][j] = 'x'
                board_copy[i + 1][j] = 'x'
                board_copy[i][j + 1] = 'x'
                put_block(board_copy)
            if board[i][j + 1] == '.' and board[i + 1][j + 1] == '.':
                flag = False
                board_copy = copy.deepcopy(board)
                print_help(board_copy)
                board_copy[i][j] = 'y'
                board_copy[i][j + 1] = 'y'
                board_copy[i + 1][j + 1] = 'y'
                put_block(board_copy)
            if board[i + 1][j] == '.' and board[i + 1][j + 1] == '.':
                flag = False
                board_copy = copy.deepcopy(board)
                board_copy[i][j] = 'z'
                board_copy[i + 1][j] = 'z'
                board_copy[i + 1][j + 1] = 'z'
                put_block(board_copy)
            break

    if flag:
        print_help(board)


num_prob = int(input())
for prob in range(num_prob):
    height, width = (int(i) for i in input().split())
    board = []
    for row in range(height):
        board.append(list(input().strip()))
    put_block(board)
