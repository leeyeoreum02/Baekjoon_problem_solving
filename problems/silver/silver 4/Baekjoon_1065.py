# https://www.acmicpc.net/problem/1065

# answer

def judge_hansu(n):
    try:
        if type(n) != int:
            raise Exception("Error: argument must be an int type")
        
        digit_list = []
        
        for digit in str(n):
            digit_list.append(int(digit))
        
        if len(digit_list) == 1:
            return 1
        
        elif len(digit_list) >= 2 and len(digit_list) % 2 == 0:
            split_point = len(digit_list) // 2
            
            digit_list_front = digit_list[ :split_point]
            digit_list_back = digit_list[split_point: ]
            
            standard_num = (digit_list_front[0] + list(reversed(digit_list_back))[0]) / 2
            judge_num_list = []
            
            for index in range(len(digit_list_front)):
                judge_num = (digit_list_front[index] + list(reversed(digit_list_back))[index]) / 2
                judge_num_list.append(judge_num)
                
            if sum(judge_num_list) / len(judge_num_list) == standard_num:
                return 1
            else:
                return 0
                
        
        else:
            split_point = len(digit_list) // 2
            
            digit_list_front = digit_list[ :split_point]
            digit_list_middle = digit_list[split_point]
            digit_list_back = digit_list[split_point + 1: ]
            
            standard_num = (digit_list_front[0] + list(reversed(digit_list_back))[0]) / 2
            judge_num_list = []
            
            for index in range(len(digit_list_front)):
                judge_num = (digit_list_front[index] + list(reversed(digit_list_back))[index]) / 2
                judge_num_list.append(judge_num)
                
            if (sum(judge_num_list) / len(judge_num_list) == standard_num) and (digit_list_middle == standard_num):
                return 1
            else:
                return 0
        
    except Exception as err:
        raise err

try:
    n = int(input())
    result = 0
    
    for num in range(1, n+1):
        result += judge_hansu(num)
        
    print(result) 
    
except Exception as err:
    print(str(err))