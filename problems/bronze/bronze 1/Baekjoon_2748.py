# https://www.acmicpc.net/problem/2748

# answer

def f(n):
    a1 = 0
    a2 = 1
    
    if type(n) != int:
        raise Exception("input parameter must be integer")
    
    if n == 0:
        print(a1)
    elif n == 1:
        print(a2)
    else:
        for num in range(n + 1):
            if num == 0:
                tmp1 = a1
            elif num == 1:
                tmp2 = a2
            else:
                tmp3 = tmp1 + tmp2
                        
                tmp1 = tmp2
                tmp2 = tmp3
                
        print(tmp3)

try:
    n = int(input())
    
    f(n)
        
except Exception as err:
    print(str(err))