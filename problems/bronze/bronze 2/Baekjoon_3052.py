# https://www.acmicpc.net/problem/3052

# answer

tmp = []

for i in range(10):
    n = int(input())
    tmp.append(n % 42)
    
result = set(tmp)
print(len(result))