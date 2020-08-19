# https://www.acmicpc.net/problem/2444

# answer

try:
    n = int(input())
    
    max_count = 2*n-1
    
    for count in range(max_count):
        if count < n:
            print(' '*((n-1)-count), '*'*(2*count+1), sep='')
        else:
            reversed_count = count - (n-1)
            print(' '*(reversed_count), '*'*(max_count - 2*reversed_count), sep='')
    
except Exception as err:
    print(str(err))