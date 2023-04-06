import math

N = int(input())
candidates = list(map(int, input().split()))
B, C = map(int, input().split())

total = 0
for candidate in candidates:
    supervisor = max(1, 1 + math.ceil((candidate-B)/C))
    total += supervisor

print(total)