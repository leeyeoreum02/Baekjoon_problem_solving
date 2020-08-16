# https://www.acmicpc.net/problem/1316

# wrong

try:
    word_count = int(input())
    word_list = []
        
    for _ in range(word_count):
        word = input()
        
        if word.isalpha() == False:
            raise Exception("from second value, you must input alphabet")

        word_list.append(word.lower())
    
    for count, word in enumerate(word_list):
        word_array = list(word)
        
        for index, value in enumerate(word_array):
            if (index >= 1) and (word_array[index - 1] == word_array[index]):
                del word_array[index]
                
        word_list[count] = ''.join(word_array)
    
    result = 0
    
    for word in word_list:
        result += 1
        
        for char in word:
            if word.count(char) > 1:
                result -= 1
                break
            
    print(result)
    
except Exception as err:
    print(str(err))

# answer

try:
    word_count = int(input())
    word_list = []
        
    for _ in range(word_count):
        word = input()
        
        if word.isalpha() == False:
            raise Exception("from second value, you must input alphabet")

        word_list.append(word.lower())
    
    for number, word in enumerate(word_list):
        count = 0
        word_array = list(word)
        
        for index, value in enumerate(word_array):
            if count == word.find(value):
                target = value
            else:
                if value == target:
                    word_array[index] = ''
            
            count += 1

        word_list[number] = ''.join(word_array)               
    
    result = 0
    
    for word in word_list:
        result += 1
        
        for char in word:
            if word.count(char) > 1:
                result -= 1
                break
            
    print(result)
    
except Exception as err:
    print(str(err))