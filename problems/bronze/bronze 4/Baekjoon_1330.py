# https://www.acmicpc.net/problem/1330

# answer

a, b = map(int, input().split())

if (a >= -10000 or a <= 10000) and (b >= -10000 or a <= 10000):
    if a > b:
        print('>')
    elif a < b:
        print('<')
    elif a == b:
        print('==')