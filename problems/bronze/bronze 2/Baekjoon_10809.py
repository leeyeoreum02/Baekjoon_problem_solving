# https://www.acmicpc.net/problem/10809

# answer

from string import ascii_lowercase

alpha_list = list(ascii_lowercase)

alpha_dict = {}

for key in alpha_list:
    alpha_dict[key] = -1

try:
    word = input()    
        
except Exception as err:
    print(str(err))
    
for char in word:
    index = word.find(char)
    alpha_dict[char] = index
    
for result in list(alpha_dict.values()):
    print(result, end=' ')