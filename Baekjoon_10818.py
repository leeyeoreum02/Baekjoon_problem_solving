# https://www.acmicpc.net/problem/10818

# answer

n = int(input())
elements = list(map(int, input().split()))
print(min(elements), max(elements))