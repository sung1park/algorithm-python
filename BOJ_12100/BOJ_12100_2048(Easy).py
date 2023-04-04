import sys


def dfs(board, N, cnt):
    global max_val
    if cnt == 5:
        max_val = max(max_val, max(map(max, board)))
        return

    for dir in ['U', 'D', 'L', 'R']:
        newboard = move(board, N, dir)
        dfs(newboard, N, cnt+1)


def move(board, N, dir):
    newboard = [[0 for _ in range(N)] for __ in range(N)]
    if dir == 'U':
        for c in range(N):
            r = 0
            for i in range(N):
                if board[i][c] != 0:
                    if newboard[r][c] == 0:
                        newboard[r][c] = board[i][c]
                    else:
                        if newboard[r][c] == board[i][c]:
                            newboard[r][c] *= 2
                            r += 1
                        else:
                            r += 1
                            newboard[r][c] = board[i][c]
    elif dir == 'D':
        for c in range(N):
            r = N-1
            for i in range(N-1, -1, -1):
                if board[i][c] != 0:
                    if newboard[r][c] == 0:
                        newboard[r][c] = board[i][c]
                    else:
                        if newboard[r][c] == board[i][c]:
                            newboard[r][c] *= 2
                            r -= 1
                        else:
                            r -= 1
                            newboard[r][c] = board[i][c]
    elif dir == 'L':
        for r in range(N):
            c = 0
            for i in range(N):
                if board[r][i] != 0:
                    if newboard[r][c] == 0:
                        newboard[r][c] = board[r][i]
                    else:
                        if newboard[r][c] == board[r][i]:
                            newboard[r][c] *= 2
                            c += 1
                        else:
                            c += 1
                            newboard[r][c] = board[r][i]
    elif dir == 'R':
        for r in range(N):
            c = N-1
            for i in range(N-1, -1, -1):
                if board[r][i] != 0:
                    if newboard[r][c] == 0:
                        newboard[r][c] = board[r][i]
                    else:
                        if newboard[r][c] == board[r][i]:
                            newboard[r][c] *= 2
                            c -= 1
                        else:
                            c -= 1
                            newboard[r][c] = board[r][i]
    else:
        print('Check your direction')
        sys.exit()

    return newboard


N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

global max_val
max_val = -sys.maxsize
dfs(board, N, 0)

print(max_val)


