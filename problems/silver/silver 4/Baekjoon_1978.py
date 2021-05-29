# https://www.acmicpc.net/problem/1978

# answer

def prime_num_test(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for div_num in range(2, n):
            if n % div_num == 0:
                return False
            
    return True

n = int(input())
n_list = list(map(int, input().split()))

result = 0

for val in n_list:
    whether_prime_num = prime_num_test(val)
    
    if whether_prime_num == True:
        result += 1
        
print(result)