# https://www.acmicpc.net/problem/2439

# answer

n = int(input())

for i in range(1, (n + 1)):
    print((' ' * (n - i)) + ('*' * i))