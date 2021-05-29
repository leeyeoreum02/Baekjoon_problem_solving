# https://www.acmicpc.net/problem/4299

# wrong_1

plus, sub = map(int, input().split())

x = (plus + sub) // 2
y = (plus - sub) // 2

if x > y:
    print(x, y)
elif x < y:
    print(y, x)
else:
    print(-1)
    
# wrong_2
    
try:
    plus, sub = map(int, input().split())

    x = (plus + sub) // 2
    y = (plus - sub) // 2

    if ((plus + sub) % 2 != 0) or ((plus - sub) % 2 != 0):
        raise Exception(-1)
        
    if x > y:
        print(x, y)
    elif x < y:
        print(y, x)
    else:
        print(x, y)
    
except Exception as err:
    print(err)
    
# wrong_3
    
try:
    plus, sub = map(int, input().split())

    x = (plus + sub) // 2
    y = (plus - sub) // 2

    if ((plus + sub) % 2 != 0) or ((plus - sub) % 2 != 0):
        raise Exception(-1)
        
    if x > y:
        print(x, y)
    elif x < y:
        print(y, x)
    else:
        print(-1)
    
except Exception as err:
    print(err)
    
# wrong_4
    
try:
    plus, sub = map(int, input().split())

    x = abs(plus + sub) // 2
    y = abs(plus - sub) // 2

    if (abs(plus + sub) % 2 != 0) or (abs(plus - sub) % 2 != 0):
        raise Exception(-1)
        
    if x > y:
        print(x, y)
    elif x < y:
        print(y, x)
    else:
        print(-1)
    
except Exception as err:
    print(err)

# answer

plus, sub = map(int, input().split())

x = (plus + sub) // 2
y = (plus - sub) // 2

if ((plus + sub) % 2 != 0) or ((plus - sub) % 2 != 0):
    print(-1)
else:
    if (x >= 0) and (y >= 0):
        if x >= y:
            print(x, y)
        else:
            print(y, x)
    else:
        print(-1)