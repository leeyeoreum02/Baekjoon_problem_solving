# https://www.acmicpc.net/problem/3004

# answer

n = int(input())

if n % 2 == 0:
    row = col = n // 2
    result = (row + 1)*(col + 1)
else:
    row = (n // 2) + 1
    col = n // 2
    result = (row + 1)*(col + 1)
    
print(result)