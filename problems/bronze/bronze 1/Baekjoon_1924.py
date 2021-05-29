# https://www.acmicpc.net/problem/1924

# answer

def day_count_generator(month, day):
    target_month = 1
    target_day = 1
    
    tmp_month = month - target_month
    tmp_day = day - target_day
    
    result_day = 0
    
    day_30_month = (4, 6, 9, 11)
    
    while tmp_month >= 0:
        if tmp_month == 0:
            result_day += tmp_day
        elif tmp_month == 2:
            result_day += 28
        elif tmp_month in day_30_month:
            result_day += 30
        else:
            result_day += 31
            
        tmp_month -= 1
        
    return result_day

x, y = map(int, input().split())

result_day = day_count_generator(x, y)

day_of_week_count = result_day % 7

if day_of_week_count == 0:
    print('MON')
elif day_of_week_count == 1:
    print('TUE')
elif day_of_week_count == 2:
    print('WED')
elif day_of_week_count == 3:
    print('THU')
elif day_of_week_count == 4:
    print('FRI')
elif day_of_week_count == 5:
    print('SAT')
elif day_of_week_count == 6:
    print('SUN')
else:
    print('?')