# https://www.acmicpc.net/problem/1297

# answer

import math

t, h_r, b_r = map(int, input().split())

b = t*h_r / math.sqrt(((b_r**2) + (h_r**2)))

h = (b_r / h_r)*b

print(int(b), int(h))