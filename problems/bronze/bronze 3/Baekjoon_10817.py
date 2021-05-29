# https://www.acmicpc.net/problem/10817

# answer

a, b, c = map(int, input().split())

tmp = [a, b, c]
tmp.remove(max(tmp))
tmp.remove(min(tmp))

for i in tmp:
    result = i

print(result)