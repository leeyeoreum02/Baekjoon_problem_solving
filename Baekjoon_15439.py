# https://www.acmicpc.net/problem/15439

# answer

n = int(input())

if n == 1:
    result = 0
else:
    result = n * (n-1)

print(result)