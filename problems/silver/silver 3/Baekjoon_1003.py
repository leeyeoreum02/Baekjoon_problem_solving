# https://www.acmicpc.net/problem/1003

# time out

class fib:
    def __init__(self):
        self.fib_0 = []
        self.fib_1 = []
    
    def __fib(self, n):
        try:    
            if type(n) == float:
                raise Exception("Error: first parameter must be an integer")
                
            if n == 0:
                self.fib_0.append(0)
                return 0
            elif n == 1:
                self.fib_1.append(1)
                return 1
            else:
                return self.__fib(n - 1) + self.__fib(n - 2)
        
        except Exception as err:
            raise err
            
    def count(self, n):
        self.__fib(n)
        
        print(len(self.fib_0), len(self.fib_1))
        
        del self.fib_0[:]
        del self.fib_1[:]
    
try:
    case = int(input())
    n_list = []
    
    obj = fib()
    
    for _ in range(case):
        n = int(input())
        n_list.append(n)
        
    for n in n_list:
        obj.count(n)
        
except Exception as err:
    print(str(err))
    
# Runtime error_1
    
import numpy as np

a1 = np.array([1, 0])
a2 = np.array([0, 1])

try:
    case = int(input())
    n_list = []
    
    for n in range(case):
        n = int(input())
        n_list.append(n)
        
        an_list = []
        
    for index in range(max(n_list) + 1):
        if index == 0:
            an_list.append(a1)
        elif index == 1:
            an_list.append(a2)
        else:
            an_list.append(an_list[index - 1] + an_list[index - 2])
                        
    for n in n_list:
        print(an_list[n][0], an_list[n][1])
        
except Exception as err:
    print(str(err))
    
# Runtime error_2
    
import numpy as np

def f(n):
    a1 = np.array([1, 0])
    a2 = np.array([0, 1])
    
    if type(n) != int:
        raise Exception("input parameter must be integer")
    
    if n == 0:
        return a1
    elif n == 1:
        return a2
    else:
        for element in range(n + 1):
            if element == 0:
                tmp1 = a1
            elif element == 1:
                tmp2 = a2
            else:
                tmp3 = tmp1 + tmp2
                        
                tmp1 = tmp2
                tmp2 = tmp3
                
        return tmp3

try:
   case = int(input())
   result_list = []
   
   for _ in range(case):
       n = int(input())
       result_list.append(f(n))
       
   
   for result in result_list:
       print(result[0], result[1]) 
        
except Exception as err:
    print(str(err))
    
# Runtime error_3
    
import numpy as np

def f(n):
    a1 = np.array([1, 0])
    a2 = np.array([0, 1])
    
    if type(n) != int:
        raise Exception("input parameter must be integer")
    
    if n == 0:
        print(a1[0], a1[1])
    elif n == 1:
        print(a2[0], a2[1])
    else:
        for element in range(n + 1):
            if element == 0:
                tmp1 = a1
            elif element == 1:
                tmp2 = a2
            else:
                tmp3 = tmp1 + tmp2
                        
                tmp1 = tmp2
                tmp2 = tmp3
                
        print(tmp3[0], tmp3[1])

try:
   case = int(input())
   result_list = []
   
   for _ in range(case):
       n = int(input())
       f(n)
        
except Exception as err:
    print(str(err))
    
# answer_1
    
a = int(input())

zero = [1, 0, 1]
one = [0, 1, 1]

def cal(num):
    length = len(zero)
    if length <= num:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print("{} {}".format(zero[num], one[num]))
    
for i in range(a):
    k = int(input())
    cal(k)

# answer_2

def f(n):
    a1 = [1, 0]
    a2 = [0, 1]
    
    if type(n) != int:
        raise Exception("input parameter must be integer")
    
    if n == 0:
        print(a1[0], a1[1])
    elif n == 1:
        print(a2[0], a2[1])
    else:
        for element in range(n + 1):
            if element == 0:
                tmp1 = a1
            elif element == 1:
                tmp2 = a2
            else:
                tmp3 = [(tmp1[0] + tmp2[0]), (tmp1[1] + tmp2[1])]
                        
                tmp1 = tmp2
                tmp2 = tmp3
                
        print(tmp3[0], tmp3[1])

try:
   case = int(input())
   
   for _ in range(case):
       n = int(input())
       f(n)
        
except Exception as err:
    print(str(err))