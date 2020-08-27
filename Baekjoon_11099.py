# https://www.acmicpc.net/problem/2530

# wrong

a, b, c = map(int, input().split())
d = int(input())

d_hour = d // 3600
d_minute = (d % 3600) // 60
d_second = (d % 3600) % 60

print(d_hour, d_minute, d_second)

tmp_hour = a + d_hour
tmp_minute = b + d_minute
tmp_second = c + d_second

if tmp_second >= 60:
    tmp_minute += tmp_second // 60
    ret_second = tmp_second % 60
else:
    ret_second = tmp_second
    
if tmp_minute >= 60:
    tmp_hour += tmp_minute // 60
    ret_minute = tmp_minute % 60
else:
    ret_minute = tmp_minute
    
if tmp_hour >= 24:
    ret_hour = tmp_hour % 24
else:
    ret_hour = tmp_hour
    
print(ret_hour, ret_minute, ret_second)

# answer

a, b, c = map(int, input().split())
d = int(input())

d_hour = d // 3600
d_minute = (d % 3600) // 60
d_second = (d % 3600) % 60

tmp_hour = a + d_hour
tmp_minute = b + d_minute
tmp_second = c + d_second

if tmp_second >= 60:
    tmp_minute += tmp_second // 60
    ret_second = tmp_second % 60
else:
    ret_second = tmp_second
    
if tmp_minute >= 60:
    tmp_hour += tmp_minute // 60
    ret_minute = tmp_minute % 60
else:
    ret_minute = tmp_minute
    
if tmp_hour >= 24:
    ret_hour = tmp_hour % 24
else:
    ret_hour = tmp_hour
    
print(ret_hour, ret_minute, ret_second)