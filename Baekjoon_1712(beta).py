# https://www.acmicpc.net/problem/1712

try:
    fixed_cost, variable_cost, price = map(int, input().split())
    
    if (fixed_cost == 0) or (variable_cost == 0) or (price == 0):
        raise Exception("input value must be larger than zero")
    
    count = 1
    
    print("fixed_cost = ", fixed_cost, "variable_cost = ", variable_cost, "price = ", price)
    
    while True:
        print("count = ", count)
        
        if (price*count) > (fixed_cost + variable_cost*count):
            print(count)
            break
        
        count += 1
            
except Exception as err:
    print(str(err))