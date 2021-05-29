# https://www.acmicpc.net/problem/2577

# answer

a = int(input())
b = int(input())
c = int(input())

result = list(map(int, list(str(a * b * c))))

for n in range(10):
    print(result.count(n))