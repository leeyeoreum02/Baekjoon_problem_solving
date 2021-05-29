# https://www.acmicpc.net/problem/10996

# answer

n = int(input())

for step_1 in range(n):
    for step_2 in range(2):
        if step_2 % 2 == 0:
            for stars in range(n):
                if stars % 2 == 0:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
        else:
            for stars in range(n):
                if stars % 2 == 0:
                    print(' ', end='')
                else:
                    print('*', end='')
            print()