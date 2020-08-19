# https://www.acmicpc.net/problem/2441

# answer

try:
    n = int(input())
    
    for count in range(n):
        print(' '*count, '*'*(n - count), sep='')
        
except Exception as err:
    print(str(err))