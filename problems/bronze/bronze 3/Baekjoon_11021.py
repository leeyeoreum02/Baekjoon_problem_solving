# https://www.acmicpc.net/problem/11021

# answer

n = int(input())
result = []

for i in range(n):
    a, b = map(int, input().split())
    result.append(a + b)

for i, j in enumerate(result):
    print("Case #{}: {}".format((i + 1), j))