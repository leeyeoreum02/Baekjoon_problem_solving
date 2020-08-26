# https://www.acmicpc.net/problem/5554

# answer

sec_list = []

for _ in range(4):
    sec = int(input())
    sec_list.append(sec)
    
x = sum(sec_list) // 60
y = sum(sec_list) % 60

print(x, y, sep='\n')