# https://www.acmicpc.net/problem/2839

# answer

n = int(input())

b = 0

while True:
    if (n - 3*b) % 5 == 0:
        a = (n - 3*b) / 5
        break
        
    b += 1

if a >= 0 and b >= 0:
    print(int(a + b))
else:
    print(-1)