# https://www.acmicpc.net/problem/15552

# answer

import sys

n = int(sys.stdin.readline().rstrip())
result = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    result.append(a + b)

for i in result:
    print(i)