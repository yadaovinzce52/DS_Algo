# num1 = 11
#
# # pointer
# num2 = num1
#
# print('Before num2 value updates:')
# print(f'num1 = {num1}')
# print(f'num2 = {num2}')
#
# print(f'\nnum1 points to: {id(num1)}')
# print(f'num2 points to: {id(num2)}')
#
# num2 = 22
#
# print('After num2 value updates:')
# print(f'num1 = {num1}')
# print(f'num2 = {num2}')
#
# print(f'\nnum1 points to: {id(num1)}')
# print(f'num2 points to: {id(num2)}')

dict1 = {
    'value': 11
}

dict2 = dict1

print('Before value updated:')
print(f'dict1 = {dict1}')
print(f'dict2 = {dict2}')

print(f'\ndict1 points to: {id(dict1)}')
print(f'dict2 points to: {id(dict1)}')

dict2['value'] = 22

print('\nAfter value updated:')
print(f'dict1 = {dict1}')
print(f'dict2 = {dict2}')

print(f'\ndict1 points to: {id(dict1)}')
print(f'dict2 points to: {id(dict1)}')

