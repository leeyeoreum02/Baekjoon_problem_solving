# https://www.acmicpc.net/problem/11720

# answer

try:
    count = int(input())
    num_array = str(input())
    
    result = 0
    
    for n in num_array:
        n = int(n)
        result += n
        
    print(result)
    
except Exception as err:
    print(str(err))