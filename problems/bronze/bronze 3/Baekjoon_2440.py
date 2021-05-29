# https://www.acmicpc.net/problem/2440

# answer

try:
    n = int(input())
    
    for count in range(n, 0, -1):
        print('*'*count)
        
except Exception as err:
    print(str(err))