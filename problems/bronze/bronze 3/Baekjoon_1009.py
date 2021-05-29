# https://www.acmicpc.net/problem/1009

# time out

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    
    data_count = a ** b
    
    print(int(str(data_count)[-1]))
    
# Runtime error_1
    
t = int(input())

last_digit_dict = {1:[1], 2:[2, 4, 8, 6], 3:[3, 9, 7, 1], 4:[4, 6], 5:[5, 0], 6:[6], 7:[7, 9, 3, 1], 8:[8, 4, 2, 6], 9:[9, 1]}

print(last_digit_dict[99%10])

for _ in range(t):
    a, b = map(int, input().split())
    
    result = last_digit_dict[a % 10][(b % len(last_digit_dict[a % 10])) - 1]
    
    print(result)
    
# Runtime error_2
    
t = int(input())

last_digit_dict = {1:[1], 2:[2, 4, 8, 6], 3:[3, 9, 7, 1], 4:[4, 6], 5:[5, 0], 6:[6], 7:[7, 9, 3, 1], 8:[8, 4, 2, 6], 9:[9, 1]}

for _ in range(t):
    a, b = map(int, input().split())
    
    result = last_digit_dict[a % 10][(b % len(last_digit_dict[a % 10])) - 1]
    
    print(result)
    
# wrong
    
t = int(input())

last_digit_dict = {1:[1], 2:[2, 4, 8, 6], 3:[3, 9, 7, 1], 4:[4, 6], 5:[5, 0], 6:[6], 7:[7, 9, 3, 1], 8:[8, 4, 2, 6], 9:[9, 1]}

for _ in range(t):
    a, b = map(int, input().split())
    
    if (a % 10) == 0:
        result = 10
    else:    
        result = last_digit_dict[a % 10][(b % len(last_digit_dict[a % 10])) - 1]
    
    print(result)

# answer

t = int(input())

last_digit_dict = {1:[1], 2:[2, 4, 8, 6], 3:[3, 9, 7, 1], 4:[4, 6], 5:[5], 6:[6], 7:[7, 9, 3, 1], 8:[8, 4, 2, 6], 9:[9, 1]}

for _ in range(t):
    a, b = map(int, input().split())
    
    if (a % 10) == 0:
        result = 10
    else:    
        result = last_digit_dict[a % 10][(b % len(last_digit_dict[a % 10])) - 1]
    
    print(result)