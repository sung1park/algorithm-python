def outOfRange(r, c, N):
    if r < 0 or r >= N or c < 0 or c >= N:
        return True
    return False


# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

snake = [(0, 0)]
apples = []
commands = []

curr_dir = 0
curr_time = 0
ended = False

N = int(input())
K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    apples.append((r-1, c-1))

L = int(input())
for _ in range(L):
    X, C = input().split()
    commands.append((int(X), C))

curr_command = commands.pop(0)
while True:
    curr_time += 1

    hx, hy = snake[-1]
    nx, ny = hx+dx[curr_dir], hy+dy[curr_dir]
    # 벽에 부딪히거나 자기자신의 몸과 부딪히는 경우
    if outOfRange(nx, ny, N) or (nx, ny) in snake:
        break

    # 다음 위치에 사과가 있을 경우 사과를 먹고 꼬리는 제자리에 있는다
    # 다음 위치에 사과가 없을 경우 꼬리는 한 칸 움직인다
    try:
        apple_index = apples.index((nx, ny))
    except ValueError:
        apple_index = -1

    if apple_index != -1:
        snake.append((nx, ny))
        apples.pop(apple_index)
    else:
        snake.append((nx, ny))
        snake.pop(0)

    if curr_time == curr_command[0]:
        next_dir = curr_command[1]
        if next_dir == 'L':
            curr_dir = (curr_dir - 1) % 4
        elif next_dir == 'D':
            curr_dir = (curr_dir + 1) % 4
        if commands:
            curr_command = commands.pop(0)

print(curr_time)
