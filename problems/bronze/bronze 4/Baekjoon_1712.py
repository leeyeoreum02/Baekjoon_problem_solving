# https://www.acmicpc.net/problem/1712

# time out_1

try:
    fixed_cost, variable_cost, price = map(int, input().split())
    
    count = 1
    
    while True:
        if (price*count) > (fixed_cost + variable_cost*count):
            print(count)
            break
        
        count += 1
            
except RuntimeError:
    print(-1)

# time out_2

try:
    fixed_cost, variable_cost, price = map(int, input().split())
    
    if (fixed_cost == 0) or (variable_cost == 0) or (price == 0):
        raise Exception("Error: input value must be larger than zero")
    
    if variable_cost >= price:
        raise Exception(-1)
    
    count = 1
    
    while True:
        if (price*count) > (fixed_cost + variable_cost*count):
            print(count)
            break
        
        count += 1
            
except Exception as err:
    print(str(err))

# answer

try:
    fixed_cost, variable_cost, price = map(int, input().split())
    
    if (fixed_cost == 0) or (variable_cost == 0) or (price == 0):
        raise Exception("Error: input value must be larger than zero")
    
    if variable_cost >= price:
        raise Exception(-1)
    
    point = int(fixed_cost / (price - variable_cost)) + 1
    
    print(point)
            
except Exception as err:
    print(err)