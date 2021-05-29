# https://www.acmicpc.net/problem/2562

# answer

tmp = []

for _ in range(9):
    n = int(input())
    tmp.append(n)
    
print(max(tmp), tmp.index(max(tmp)) + 1, sep=' ')