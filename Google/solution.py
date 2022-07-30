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


def common_item(arr1, arr2) -> bool:
    for item in arr1:       # O(N) looping through
        if item in arr2:    # O(M)
            return True

    return False


test_arr1 = ['a', 'b', 'c', 'x']
test_arr2 = ['z', 'y', 'i']

test_arr3 = ['a', 'b', 'c', 'x']
test_arr4 = ['z', 'y', 'x']

print(common_item(test_arr1, test_arr2))
print(common_item(test_arr3, test_arr4))

# Time complexity = O(N * M)
# Space complexity = O(1)

# Faster method
