# https://www.acmicpc.net/problem/10872

# wrong

def fac(n):
    for tmp in range(1, (n+1)):
        if tmp == 1:
            result = tmp
        else:
            result *= tmp
            
    return result

try:
    n = int(input())
    
    print(fac(n))
    
except Exception as err:
    print(str(err))

# answer

def fac(n):
    if n == 0:
        return 1
    else:
        for tmp in range(1, (n+1)):
            if tmp == 1:
                result = tmp
            else:
                result *= tmp
            
        return result

try:
    n = int(input())
    
    print(fac(n))
    
except Exception as err:
    print(err)