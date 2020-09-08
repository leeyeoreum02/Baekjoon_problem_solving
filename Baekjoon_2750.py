# https://www.acmicpc.net/problem/2750

# answer

n = int(input())

tmp_list = []

for _ in range(n):
    num = int(input())
    tmp_list.append(num)
    
result_list = sorted(tmp_list)

for result in result_list:
    print(result)