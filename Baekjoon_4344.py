# https://www.acmicpc.net/problem/4344

# answer

case_num = int(input())
case_list = []

for _ in range(case_num):
    input_test_case = list(map(int, input().split()))
    case_list.append(input_test_case)
    
total = 0
for test_case in case_list:
    for index in range(1, len(test_case)):
        total += test_case[index]
        mean = total / test_case[0]
        
        good_student_num = 0
        for index in range(1, len(test_case)):
            if test_case[index] > mean:
                good_student_num += 1
                
    print('{:.3f}%'.format(round(good_student_num / (len(test_case) - 1) * 100, 4)))
    total = 0
    good_student_num = 0