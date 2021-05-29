# https://www.acmicpc.net/problem/2588

# Runtime error_1

a, b = input().split('\n')
print(int(a) * int(b[-1]))
print(int(a) * int(b[-2]))
print(int(a) * int(b[-3]))
print(int(a) * int(b))

# Runtime error_2

a, b = input().split()
print(int(a) * int(b[-1]))
print(int(a) * int(b[-2]))
print(int(a) * int(b[-3]))
print(int(a) * int(b))

# answer

a = input()
b = input()
print(int(a) * int(b[-1]))
print(int(a) * int(b[-2]))
print(int(a) * int(b[-3]))
print(int(a) * int(b))