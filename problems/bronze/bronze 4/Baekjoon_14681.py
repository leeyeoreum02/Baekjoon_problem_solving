# https://www.acmicpc.net/problem/14681

# answer

x = int(input())
y = int(input())

if (x >= -1000 and x <= 1000 and x != 0) and (y >= -1000 and y <= 1000 and y != 0):
    if x > 0 and y > 0:
        print('1')
    elif x < 0 and y > 0:
        print('2')
    elif x < 0 and y < 0:
        print('3')
    elif x > 0 and y < 0:
        print('4')