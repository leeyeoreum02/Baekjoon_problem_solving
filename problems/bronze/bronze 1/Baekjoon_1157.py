# https://www.acmicpc.net/problem/1157

# time out_1

try:
    word = input().upper()
    
    if word.isalpha() == False:
        raise Exception("input value must be an alphabet")
    
except Exception as err:
    print(err)
    
word_count_dict = {}

for char in word:
    word_count_dict[char] = word.count(char)

max_key = max(word_count_dict, key=lambda k: word_count_dict[k])
max_value = max(word_count_dict.values())

if list(word_count_dict.values()).count(max_value) > 1:
    print("?")
else:
    print(max_key)
    
# time out_2
    
try:
    word = input().upper()
    
    if word.isalpha() == False:
        raise Exception("input value must be an alphabet")
        
    word_count_dict = {}

    for char in word:
        word_count_dict[char] = word.count(char)

    max_key = max(word_count_dict, key=lambda k: word_count_dict[k])
    value_list = list(word_count_dict.values())
    max_value = max(value_list)
    
    if value_list.count(max_value) > 1:
        print("?")
    else:
        print(max_key)
    
except Exception as err:
    print(err)
    
# time out_3
    
import operator

try:
    word = input().upper()
    
    if word.isalpha() == False:
        raise Exception("input value must be an alphabet")
        
    word_count_dict = {}

    for char in word:
        word_count_dict[char] = word.count(char)

    max_key = max(word_count_dict.items(), key=operator.itemgetter(1))[0]
    value_list = list(word_count_dict.values())
    max_value = max(value_list)
    
    if value_list.count(max_value) > 1:
        print("?")
    else:
        print(max_key)
    
except Exception as err:
    print(str(err))
    
# time out_4
    
try:
    word = input().upper()
    
    if word.isalpha() == False:
        raise Exception("input value must be an alphabet")
        
    word_count_dict = {}

    for char in word:
        word_count_dict[char] = word.count(char)
        
    max_value = max(word_count_dict.values())
    max_key = None
    max_value_list = []

    for key, val in word_count_dict.items():
        if val == max_value:
            max_key = key
            max_value_list.append(val)
            
    if max_value_list.count(max_value) > 1:
        print("?")
    else:
        print(max_key)
    
except Exception as err:
    print(str(err))
    
# time out_5
    
word = input().upper()
       
word_count_dict = {}

for char in word:
    word_count_dict[char] = word.count(char)
        
max_value = max(word_count_dict.values())
max_key = None
max_value_list = []

for key, val in word_count_dict.items():
    if val == max_value:
        max_key = key
        max_value_list.append(val)
            
if max_value_list.count(max_value) > 1:
    print("?")
else:
    print(max_key)
    
# answer_1
    
from collections import Counter

word = input().upper()
word_count_dict = Counter(word)

max_value = max(word_count_dict.values())
max_key = None
max_value_list = []

for key, val in word_count_dict.items():
    if val == max_value:
        max_key = key
        max_value_list.append(val)
            
if max_value_list.count(max_value) > 1:
    print("?")
else:
    print(max_key)
    
# answer_2
    
try:
    from collections import Counter
    
    word = input().upper()
    
    if word.isalpha() == False:
        raise Exception("input value must be alphabet")
        
    word_count_dict = Counter(word)
    
    max_value = max(word_count_dict.values())
    max_key = max(word_count_dict.keys(), key=(lambda k: word_count_dict[k]))
    value_list = list(word_count_dict.values())
                
    if value_list.count(max_value) > 1:
        print("?")
    else:
        print(max_key)

except Exception as err:
    print(str(err))