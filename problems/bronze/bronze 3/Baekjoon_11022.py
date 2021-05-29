# https://www.acmicpc.net/problem/11022

# answer

n = int(input())
result = []
list_a = []
list_b = []

for i in range(n):
    a, b = map(int, input().split())
    result.append(a + b)
    list_a.append(a)
    list_b.append(b)

for i, j in enumerate(result):
    print("Case #{}: {} + {} = {}".format((i + 1), list_a[i], list_b[i], j))