# https://www.acmicpc.net/source/20369550

# wrong_1

H, M = map(int, input().split())

if (H >= 0 and H <= 23) and (M >= 0 and M <= 59):
    if (H > 0 and H <= 23) and (M >= 0 and M < 45):
        H -= 1
        M += 15
    elif (H == 0) and (M >= 0 and M <= 59):
        H = 23
        M += 15
    elif M >= 45 and M <= 59:
        M -= 45
    print("{} {}".format(H, M))
    
# wrong_2
    
H, M = map(int, input().split())

if (H >= 0 and H <= 23) and (M >= 0 and M <= 59):
    if (H > 0 and H <= 23) and (M >= 0 and M < 45):
        H -= 1
        M += 15
    elif (H == 0) and (M >= 0 and M <= 45):
        H = 23
        M += 15
    elif M >= 45 and M <= 59:
        M -= 45
    print("{} {}".format(H, M))
    
# answer_1
    
H, M = map(int, input().split())

if (H >= 0 and H <= 23) and (M >= 0 and M <= 59):
    if (H > 0 and H <= 23) and (M >= 0 and M < 45):
        H -= 1
        M += 15
    elif (H == 0) and (M >= 0 and M < 45):
        H = 23
        M += 15
    elif M >= 45 and M <= 59:
        M -= 45
    print("{} {}".format(H, M))
    
# answer_2
    
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
        
# answer_3
        
H, M = map(int, input().split())
        
if M >= 45 and M <= 59:
    M -= 45
elif (H > 0 and H <= 23) and (M >= 0 and M < 45):
    H -= 1
    M += 15
elif (H == 0) and (M >= 0 and M < 45):
    H = 23
    M += 15
    
print("{} {}".format(H, M))