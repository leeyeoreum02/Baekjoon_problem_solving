# https://www.acmicpc.net/problem/15727

# wrong

l = int(input())

result = (l // 5) + 1

print(result)

# answer

l = int(input())

if l % 5 == 0:
    result = (l // 5)
else:
    result = (l // 5) + 1

print(result)