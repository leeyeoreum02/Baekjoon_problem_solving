# https://www.acmicpc.net/problem/2908

# answer

try:
    a, b = input().split()
    
    if a.isdigit() == False or b.isdigit() == False:
        raise Exception("you must input integer")
        
    reversed_a = list(reversed(list(a)))
    reversed_b = list(reversed(list(b)))
    
    result_a = int(''.join(reversed_a))
    result_b = int(''.join(reversed_b))
    
    if result_a > result_b:
        print(result_a)
    else:
        print(result_b)

except Exception as err:
    print(str(err))