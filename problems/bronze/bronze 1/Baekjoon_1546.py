# https://www.acmicpc.net/problem/1546

# answer

num = int(input())
before = list(map(int, input().split()))
    
after = [score / max(before) * 100 for score in before]
print(sum(after) / len(after))