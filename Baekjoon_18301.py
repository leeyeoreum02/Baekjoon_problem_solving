# https://www.acmicpc.net/problem/18301

# answer

n1, n2, n12 = map(int, input().split())

result = int(((n1 + 1)*(n2 + 1) / (n12 + 1) - 1))

print(result)