# https://www.acmicpc.net/problem/1271

# wrong

n, m = map(int, input().split())

q = n // m

r = n % n

print(q, r, sep='\n')

# answer

n, m = map(int, input().split())

q = n // m

r = n % m

print(q, r, sep='\n')