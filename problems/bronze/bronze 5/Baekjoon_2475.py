# https://www.acmicpc.net/problem/2475

# answer

num_list = list(map(int, input().split()))

result = 0

for index, value in enumerate(num_list):
    result += (value ** 2)

result %= 10
    
print(result)