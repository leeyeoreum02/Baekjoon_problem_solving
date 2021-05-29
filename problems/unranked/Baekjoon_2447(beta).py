# https://www.acmicpc.net/problem/2447

# answer

def star(n):
    import math
    
    if n <= 0:
        raise Exception("Error: input parameter must be more than zero")
    
    if str(math.log(n, 3))[len(str(math.log(n, 3))) - 1] == 0:
        raise Exception("Error: input parameter must be a power of three")
    
    if n == 3:
        return '***\n* *\n***'
            
    else:
        for col in range(3):
            for row in range(3):
                if col != 1 or row != 1:
                    print(star(n//3), sep='', end='')
                    
            print()
                    
        n //= 3
        
try:
    star(9)
    
except Exception as err:
    print(str(err))