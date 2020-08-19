# https://www.acmicpc.net/problem/2445

# wrong

try:
    n = int(input())
    
    max_count = 2*n-1
    
    for count in range(max_count):
        if count < (n-1):
            print('*'*(count+1), ' '*(max_count - 2*(count+1)), '*'*(count+1), sep='')
        elif count == (n-1):
            print('*'*max_count)
        else:
            reversed_count = max_count - count
            print('*'*(reversed_count), ' '*(max_count - 2*reversed_count), '*'*(reversed_count), sep='')
    
except Exception as err:
    print(str(err))

# answer

try:
    n = int(input())
    
    max_count = 2*n-1
    
    for count in range(max_count):
        if count < (n-1):
            print('*'*(count+1), ' '*((max_count+1) - 2*(count+1)), '*'*(count+1), sep='')
        elif count == (n-1):
            print('*'*(max_count+1))
        else:
            reversed_count = max_count - count
            print('*'*(reversed_count), ' '*((max_count+1) - 2*reversed_count), '*'*(reversed_count), sep='')
    
except Exception as err:
    print(str(err))