# https://www.acmicpc.net/problem/17496

# answer

n, t, c, p = map(int, input().split())

result = ((n-1) // t)*c*p

print(result)