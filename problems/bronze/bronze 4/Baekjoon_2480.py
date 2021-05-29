# https://www.acmicpc.net/problem/2480

# answer

f, s, t = map(int, input().split())

check_list = [f, s, t]

check_set = set(check_list)

if len(check_set) == 1:
    result = 10000 + f*1000
elif len(check_set) == 2:
    for element in check_set:
        if check_list.count(element) == 2:
            result = 1000 + element*100
else:
    result = max(check_list)*100
    
print(result)