# https://www.acmicpc.net/problem/14652

# answer

N, M, k = map(int, input().split())

n = k // M

m = k % M

print(n, m, sep=' ')