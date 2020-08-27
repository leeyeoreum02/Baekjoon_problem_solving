# https://www.acmicpc.net/problem/2752

# answer

n_list = list(map(int, input().split()))

result = sorted(n_list)

for val in result:
    print(val, end=' ')