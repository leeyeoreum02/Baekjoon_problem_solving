# https://www.acmicpc.net/problem/1212

# output exceeded

n = int(input(), 8)

result = list(bin(n))

print(result)

result = int(''.join(result[2:]))

print(result)

# timeout

n = int(input(), 8)

result = list(bin(n))

result = int(''.join(result[2:]))

print(result)

# wrong

n = int(input(), 8)

print(bin(n))

# answer

n = int(input(), 8)

result = list(bin(n))

result = ''.join(result[2:])

print(result)