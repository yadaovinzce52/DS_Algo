"""
Given 2 arrays, create a function that
lets a user know (True/False) whether
these two arrays contain any common items
For Example:
    array_1 = ['a', 'b', 'c', 'x']
    array_2 = ['z', 'y', 'i']
should return False
------------
    array_1 = ['a', 'b', 'c', 'x']
    array_2 = ['z', 'y', 'x']
should return True
"""

# "contain ANY items"
# This means once we find a common item we can return True
# must have 2 inputs (2 arrays)

# # Brute Force
# def common_item(arr1, arr2) -> bool:
#     for item in arr1:       # O(N) looping through
#         if item in arr2:    # O(M)
#             return True
#
#     return False
# # Time complexity = O(N * M)
# # Space complexity = O(1)


# FASTER METHOD
def common_item(arr1, arr2) -> bool:
    # dictionary = {}       # O(N) space
    # for element in arr1:        # O(N) time
    #     dictionary[element] = 1

    dictionary = {element: 1 for element in arr1}       # Still O(N) but list comprehension makes code more compact

    for element in arr2:        # O(M) time
        if dictionary.get(element) == 1:      # O(1) time
            return True

    return False
# Time complexity = O(N + M)
# Space complexity = Max(N, M)


test_arr1 = ['a', 'b', 'c', 'x']
test_arr2 = ['z', 'y', 'i']

test_arr3 = ['a', 'b', 'c', 'x']
test_arr4 = ['z', 'y', 'x']

test_arr5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_arr6 = [11, 22, 33, 44, 55, 6, 7, 88, 9]

print(common_item(test_arr1, test_arr2))
print(common_item(test_arr3, test_arr4))
print(common_item(test_arr5, test_arr6))
