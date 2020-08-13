# https://www.acmicpc.net/problem/4673

# answer

def d(n):
    try:
        digit_sum = 0
    
        for digit in str(n):
            digit_sum += int(digit)
        
        return n + digit_sum
    
    except Exception as err:
        raise err

try:
    n = 1
    d_list = []
    
    while True:
        if n > 10000:
            break
        
        d_list.append(d(n))
        n += 1
        
except Exception as err:
    print(str(err))
    
for result in range(1, 10001):
    if result not in d_list:
        print(result)