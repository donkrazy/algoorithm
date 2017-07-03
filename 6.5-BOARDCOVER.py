def put_block(board):
    changed = False
    height = len(board)
    width = len(board[0])
    ret = 0

    for i in range(height):
        for j in range(width):
            # some block already exist
            if board[i][j] != '.':
                continue

            # in edge
            if i == height - 1 or j == width - 1:
                in_edge = True
            else:
                in_edge = False

            # ┌ shape
            if not in_edge and board[i][j + 1] == '.' and board[i + 1][j] == '.':
                changed = True
                board[i][j] = 'x'
                board[i + 1][j] = 'x'
                board[i][j + 1] = 'x'
                ret += put_block(board)
                board[i][j] = '.'
                board[i + 1][j] = '.'
                board[i][j + 1] = '.'
            # ┐ shape
            if not in_edge and board[i][j + 1] == '.' and board[i + 1][j + 1] == '.':
                changed = True
                board[i][j] = 'y'
                board[i][j + 1] = 'y'
                board[i + 1][j + 1] = 'y'
                ret += put_block(board)
                board[i][j] = '.'
                board[i][j + 1] = '.'
                board[i + 1][j + 1] = '.'
            # └ shape
            if not in_edge and board[i + 1][j] == '.' and board[i + 1][j + 1] == '.':
                changed = True
                board[i][j] = 'z'
                board[i + 1][j] = 'z'
                board[i + 1][j + 1] = 'z'
                ret += put_block(board)
                board[i][j] = '.'
                board[i + 1][j] = '.'
                board[i + 1][j + 1] = '.'
            # ┘ shape
            # exception: ['#.', '..']
            if j > 0 and i < height - 1 and board[i + 1][j] == '.' and board[i + 1][j - 1] == '.':
                changed = True
                board[i][j] = 'w'
                board[i + 1][j] = 'w'
                board[i + 1][j - 1] = 'w'
                ret += put_block(board)
                board[i][j] = '.'
                board[i + 1][j] = '.'
                board[i + 1][j - 1] = '.'
            if changed:
                return ret

    if not changed:
        for row in board:
            if '.' in row:
                return 0
        # print_help(board)
        return 1


num_prob = int(input())
for prob in range(num_prob):
    height, width = (int(i) for i in input().split())
    board = []
    for i in range(height):
        board.append(list(input().strip()))

    # Specific case
    num_dot = 0
    for row in board:
        num_dot += row.count('.')
    if num_dot % 3 != 0:  # impossible
        print(0)
        continue
    if num_dot == 0:  # all black
        print(1)
        continue

    print(put_block(board))
