# https://www.acmicpc.net/problem/10869

# wrong

a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

# answer

a, b = map(int, input().split())

if (a >= 1 or a <= 10000) and (b >= 1 or b <= 10000):
    print(a + b)
    print(a - b)
    print(a * b)
    print(int(a / b))
    print(a % b)