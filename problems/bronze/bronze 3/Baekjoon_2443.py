# https://www.acmicpc.net/problem/2443

# wrong output format

try:
    n = int(input())
    
    max_count = 2*n-1
    
    for count in range(n):
        print(' '*count, '*'*(max_count - 2*count))
    
except Exception as err:
    print(str(err))

# answer

try:
    n = int(input())
    
    max_count = 2*n-1
    
    for count in range(n):
        print(' '*count, '*'*(max_count - 2*count), sep='')
    
except Exception as err:
    print(str(err))