# https://www.acmicpc.net/problem/2941

# answer

word = input()

cro_alphabet_dict = {'c=':0, 'c-':0, 'dz=':0, 'd-':0, 'lj':0, 'nj':0, 's=':0, 'z=':0}

for key in cro_alphabet_dict.keys():
    cro_alphabet_dict[key] += word.count(key)
    
if cro_alphabet_dict['z='] > 0 and cro_alphabet_dict['dz='] > 0:
    cro_alphabet_dict['z='] -= cro_alphabet_dict['dz=']
    
result = len(word)

for key, value in cro_alphabet_dict.items():
    if key == 'dz=':
        result -= (2*value)
    else:
        result -= value
        
print(result)