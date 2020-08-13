# https://www.acmicpc.net/problem/2523

# output exceeded

n = int(input())

for i in range(1, n + 1):
    print('*' * i + ' ' * (n - i))
    
for j in range(1, n):
    print('*' * (n - j) + ' ' * n)
    
# answer
    
n = int(input())
space = 2

for i in range(1, 2*n):
    if i < n:
        print('*' * i)
    elif i == n:
        print('*' * n)
    elif i > n:
        print('*' * (i - space))
        space += 2