def outOfRange(r, c, N, M):
    if r<0 or r>=N or c<0 or c>=M:
        return True
    return False


def rollTheDice(dice, status, dir):
    curr = dice[status]
    # 북, 남, 서, 동
    if dir == 3:
        next = (curr.index('S'), status[1])
    elif dir == 4:
        next = (curr.index('N'), status[1])
    elif dir == 2:
        next = (status[1], curr.index('D'))
    elif dir == 1:
        next = (curr.index('W'), status[0])
    return next


# 동, 서, 북, 남
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

# (위쪽, 동쪽) 주사위 상태와 주사위 방향에 해당하는 숫자를 매칭
dice = {
    (1, 2): ['', 'U', 'E', 'S', 'N', 'W', 'D'],
    (1, 3): ['', 'U', 'N', 'E', 'W', 'S', 'D'],
    (1, 4): ['', 'U', 'S', 'W', 'E', 'N', 'D'],
    (1, 5): ['', 'U', 'W', 'N', 'S', 'E', 'D'],
    (2, 1): ['', 'E', 'U', 'N', 'S', 'D', 'W'],
    (2, 3): ['', 'S', 'U', 'E', 'W', 'D', 'N'],
    (2, 4): ['', 'N', 'U', 'W', 'E', 'D', 'S'],
    (2, 6): ['', 'W', 'U', 'S', 'N', 'D', 'E'],
    (3, 1): ['', 'E', 'S', 'U', 'D', 'N', 'W'],
    (3, 2): ['', 'N', 'E', 'U', 'D', 'W', 'S'],
    (3, 5): ['', 'S', 'W', 'U', 'D', 'E', 'N'],
    (3, 6): ['', 'W', 'N', 'U', 'D', 'S', 'E'],
    (4, 1): ['', 'E', 'N', 'D', 'U', 'S', 'W'],
    (4, 2): ['', 'S', 'E', 'D', 'U', 'W', 'N'],
    (4, 5): ['', 'N', 'W', 'D', 'U', 'E', 'S'],
    (4, 6): ['', 'W', 'S', 'D', 'U', 'N', 'E'],
    (5, 1): ['', 'E', 'D', 'S', 'N', 'U', 'W'],
    (5, 3): ['', 'N', 'D', 'E', 'W', 'U', 'S'],
    (5, 4): ['', 'S', 'D', 'W', 'E', 'U', 'N'],
    (5, 6): ['', 'W', 'D', 'N', 'S', 'U', 'E'],
    (6, 2): ['', 'D', 'E', 'N', 'S', 'W', 'U'],
    (6, 3): ['', 'D', 'S', 'E', 'W', 'N', 'U'],
    (6, 4): ['', 'D', 'N', 'W', 'E', 'S', 'U'],
    (6, 5): ['', 'D', 'W', 'S', 'N', 'E', 'U']
}

N, M, x, y, K = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

curr_dice = (1, 3)
cx, cy = x, y

dice_num = [-1, 0, 0, 0, 0, 0, 0]
moves = list(map(int, input().split()))
for move in moves:
    nx = cx + dx[move]
    ny = cy + dy[move]
    if outOfRange(nx, ny, N, M):
        continue

    next_dice = rollTheDice(dice, curr_dice, move)
    print(dice_num[next_dice[0]])

    bottom_index = dice[next_dice].index('D')
    if board[nx][ny] == 0:
        board[nx][ny] = dice_num[bottom_index]
    else:
        dice_num[bottom_index] = board[nx][ny]
        board[nx][ny] = 0

    cx, cy = nx, ny
    curr_dice = next_dice
