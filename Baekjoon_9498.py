# https://www.acmicpc.net/problem/9498

# wrong

score = int(input())

if score >= 90 or score <= 100:
    print('A')
elif score >= 80 or score <= 89:
    print('B')
elif score >= 70 or score <= 79:
    print('C')
elif score >= 60 or score <= 69:
    print('D')
else:
    print('F')
    
# answer
    
score = int(input())

if score >= 90 and score <= 100:
    print('A')
elif score >= 80 and score <= 89:
    print('B')
elif score >= 70 and score <= 79:
    print('C')
elif score >= 60 and score <= 69:
    print('D')
else:
    print('F')