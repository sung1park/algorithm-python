import sys

N, K = map(int, sys.stdin.readline().split())

items = list()
for _ in range(N):
    w, v = map(int, sys.stdin.readline().split())
    items.append((w, v))
items.sort(key=lambda x: (x[0], x[1]))

D = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    w, v = items[i-1]
    for j in range(K+1):
        if j >= w:
            D[i][j] = max(D[i-1][j-w] + v, D[i-1][j])
        else:
            D[i][j] = D[i-1][j]

print(D[-1][-1])