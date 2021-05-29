from collections import deque

clock = deque()

for hours in range(24):
    for minutes in range(60):
         clock.append('{} {}'.format(hours, minutes))
         
H, M = input().split()

present_time = '{} {}'.format(H, M)

for index in range(len(clock)):
    if present_time == clock[index]:
        print(clock[index - 45])