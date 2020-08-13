# https://www.acmicpc.net/problem/8958

# answer

n = int(input())
OX_list = []

for _ in range(n):
    OX = input()
    OX_list.append(OX)

score = 0
combo = 1
for OX in OX_list:
    for element in OX:
        if element == 'O':
            score += combo
            combo += 1
        else:
            combo = 1
    print(score)
    score = 0
    combo = 1