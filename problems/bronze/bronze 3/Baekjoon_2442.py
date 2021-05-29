# https://www.acmicpc.net/problem/2442

# wrong output format

try:
    n = int(input())
    
    max_count = 2*n - 1
    
    for count in range((n-1), -1, -1):
        print(' '*count, '*'*(max_count - 2*count), ' '*count, sep='')
    
except Exception as err:
    print(str(err))

# answer

try:
    n = int(input())
    
    max_count = 2*n - 1
    
    for count in range((n-1), -1, -1):
        print(' '*count, '*'*(max_count - 2*count), sep='')
    
except Exception as err:
    print(str(err))