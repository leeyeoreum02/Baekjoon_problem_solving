# https://www.acmicpc.net/problem/10871

# answer

N, X = map(int, input().split())
A = list(map(int, input().split()))

for index in range(len(A)):
    if index >= N:
        del A[index]

result = [i for i in A if i < X]

for i in result:
    print(i, end=' ')