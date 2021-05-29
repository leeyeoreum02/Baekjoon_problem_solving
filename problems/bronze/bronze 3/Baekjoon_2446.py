# https://www.acmicpc.net/problem/2446

# answer

n = int(input())

for i in range(2*n - 1):
    if i < n:
        print(' ' * i + '*' * (2*n - 1 - 2*i))
    elif i >= n:
        print(' ' * (n - i + (n - 2)) + '*' * (3 + 2*(i - n)))