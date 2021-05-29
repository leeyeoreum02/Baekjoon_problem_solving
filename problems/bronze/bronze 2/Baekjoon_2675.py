# https://www.acmicpc.net/problem/2675

# answer

def get_case():
    try:
        case_count = int(input())
        case_list = []
        
        for count in range(case_count):
            case = input().split()
            
            if (len(case) == 2) and (case[0].isdigit() == True):
                case_list.append(case)
            else:
                raise Exception("you must input only repeat count and QR CODE alphanumeric character array or first element must be an int type")
                
        return case_list
        
    except Exception as err:
        raise err
        
while True:
    try:
        case_list = get_case()
        break

    except Exception as err:
        print(str(err), '\n')
        print("get back to the beginning ... \n")
        
extended_char_list = []
        
for case in case_list:
    for char in case[1]:
        extended_char_list.append(char*int(case[0]))
        
    result = ''.join(extended_char_list)
    print(result)
    del extended_char_list[:]