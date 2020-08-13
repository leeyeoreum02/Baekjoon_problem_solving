# https://www.acmicpc.net/problem/10950

# answer

case_number = int(input())
answer_list = []

for _ in range(case_number):
    a, b = map(int, input().split())
    answer_list.append(a + b)
    
for index in range(len(answer_list)):
    print(answer_list[index])