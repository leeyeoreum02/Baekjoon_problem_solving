# https://www.acmicpc.net/problem/8393

# answer

n = int(input())
total = 0

for i in range(1, (n + 1)):
    total += i

print(total)