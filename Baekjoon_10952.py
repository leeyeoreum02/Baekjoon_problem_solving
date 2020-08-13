# https://www.acmicpc.net/problem/10952

# answer

result = []
while True:
    a, b = map(int, input().split())

    if a == 0 and b == 0:
        break
    else:
        result.append(a + b)

for i in result:
    print(i)