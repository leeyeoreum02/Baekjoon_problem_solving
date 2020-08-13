# https://www.acmicpc.net/problem/10430

# answer

a, b, c = map(int, input().split())

if (a >= 2 or a <= 10000) and (b >= 1 or b <= 10000) and (c >= 1 or c <= 10000):
    print((a + b) % c)
    print(((a % c) + (b % c)) % c)
    print((a * b) % c)
    print(((a % c) * (b % c)) % c)