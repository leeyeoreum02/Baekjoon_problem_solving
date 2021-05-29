# https://www.acmicpc.net/problem/5522

# answer

n_list = []

for _ in range(5):
    n = int(input())
    n_list.append(n)
    
print(sum(n_list))