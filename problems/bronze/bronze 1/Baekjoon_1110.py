# https://www.acmicpc.net/problem/1110

# wrong_1

num = int(input())

if num < 10:
    num *= 10

new_num = 0
cycle = 0
input_num = num

while num != new_num:
    each_digit = []
    for index in range(len(str(input_num))):
        each_digit.append(str(input_num)[index])
        each_digit = list(map(int, each_digit))
        
    sum_each_digit = sum(each_digit)
    
    new_num = ((input_num % 10) * 10) + (sum_each_digit % 10)
    input_num = new_num
    cycle += 1
    
print(cycle)

# answer_1

n = num = int(input())
count = 0
while True:
    ten = n // 10
    one = n % 10
    total = ten + one
    count += 1
    n = int(str(n % 10) + str(total % 10))
    if(num == n):
        break
print(count)

# wrong_2

def get_num(num):
    if num < 10:
        num *= 10

    new_num = 0
    cycle = 0
    input_num = num

    while num != new_num:
        each_digit = []
        for index in range(len(str(input_num))):
            each_digit.append(str(input_num)[index])
            each_digit = list(map(int, each_digit))
        
        sum_each_digit = sum(each_digit)
    
        new_num = ((input_num % 10) * 10) + (sum_each_digit % 10)
        input_num = new_num
        cycle += 1
        
    return cycle

num = int(input())
print(get_num(num))

# answer_2

def get_num(num):
    if num < 10:
        num *= 10

    new_num = None
    cycle = 0
    input_num = num

    while num != new_num:
        each_digit = []
        for index in range(len(str(input_num))):
            each_digit.append(str(input_num)[index])
            each_digit = list(map(int, each_digit))
        
        sum_each_digit = sum(each_digit)
    
        new_num = ((input_num % 10) * 10) + (sum_each_digit % 10)
        input_num = new_num
        cycle += 1
        
    return cycle

num = int(input())
print(get_num(num))

# answer_3

num = int(input())

if num < 10:
    num *= 10

new_num = None
cycle = 0
input_num = num

while num != new_num:
    each_digit = []
    for index in range(len(str(input_num))):
        each_digit.append(str(input_num)[index])
        each_digit = list(map(int, each_digit))
        
    sum_each_digit = sum(each_digit)
    
    new_num = ((input_num % 10) * 10) + (sum_each_digit % 10)
    input_num = new_num
    cycle += 1
    
print(cycle)

# answer_4

def get_num(num):
    if num < 10:
        num *= 10

    cycle = 0
    input_num = num

    while True:
        each_digit = []
        for index in range(len(str(input_num))):
            each_digit.append(str(input_num)[index])
            each_digit = list(map(int, each_digit))
        
        sum_each_digit = sum(each_digit)
    
        new_num = ((input_num % 10) * 10) + (sum_each_digit % 10)
        input_num = new_num
        cycle += 1
        
        if num == new_num:
            break
        
    return cycle

num = int(input())
print(get_num(num))