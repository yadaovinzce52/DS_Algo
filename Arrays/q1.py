# """
# Create a function that reverses a string:
# 'Hi My name is Vinzce' should be:
# 'eczniV si eman yM iH'
# """
#
#
# def reverse(sentence: str):
#     if type(sentence) != str:
#         raise TypeError('Input must be a string.')
#
#     if len(sentence) < 2 or not sentence:
#         return sentence
#
#     # char_array = list(sentence)
#     # left = 0
#     # right = len(sentence) - 1
#     #
#     # while left < right:
#     #     temp = char_array[right]
#     #     char_array[right] = char_array[left]
#     #     char_array[left] = temp
#     #     left += 1
#     #     right -= 1
#     # Time: O(N)
#     # Space: O(N)
#
#     backwards = []
#     for char in sentence[::-1]:
#         backwards.append(char)
#     # Time: O(N)
#     # Space: O(N)
#
#     return ''.join(backwards)
#
#
# print(reverse('Hi My name is Vinzce'))
a = b = True

print(a == not b)
print(a == (not b))
print(not(a == b))
print(not a == b)