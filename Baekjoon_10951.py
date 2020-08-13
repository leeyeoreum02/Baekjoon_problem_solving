# https://www.acmicpc.net/problem/10951

# Runtime error_1

result = []

while True:
    a = list(map(int, input().split()))
    
    if a == []:
        break
    else:
        result.append(sum(a))
    
for i in result:
    print(i)
    
# Runtime error_2
    
while True:
    a, b = list(map(int, input().split()))
    print(a + b)
    
# answer
    
try:
    temp = []
    
    while True:
        a, b = map(int, input().split())
        temp.append(a + b)
except:
    for i in temp:
        print(i)
