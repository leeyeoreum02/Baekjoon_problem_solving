# https://www.acmicpc.net/problem/10953

# answer

try:
    case = int(input())
    
    result_list = []
    
    for _ in range(case):
        a, b = map(int, input().split(','))
        result_list.append(a + b)
        
    for result in result_list:
        print(result)
        
except Exception as err:
    print(str(err))