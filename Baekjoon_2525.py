# https://www.acmicpc.net/problem/2525

# wrong

a, b = map(int, input().split())
c = int(input())

c_hour = c // 60
c_minute = c % 60

ret_hour = a + c_hour
ret_minute = b + c_minute

if ret_minute >= 60:
    ret_minute %= 60
    ret_hour += ret_minute // 60

if ret_hour >= 24:
    ret_hour %= 24
    
print(ret_hour, ret_minute)

# answer

a, b = map(int, input().split())
c = int(input())

c_hour = c // 60
c_minute = c % 60

tmp_hour = a + c_hour
tmp_minute = b + c_minute

if tmp_minute >= 60:
    ret_minute = tmp_minute % 60
    tmp_hour += tmp_minute // 60
else:
    ret_minute = tmp_minute
    
if tmp_hour >= 24:
    ret_hour = tmp_hour % 24
else:
    ret_hour = tmp_hour
       
print(ret_hour, ret_minute)