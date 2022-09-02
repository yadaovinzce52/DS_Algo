# [0,3,4,31], [4,6,30]
# result should be [0,3,4,4,6,30,31]


def merge_sorted_array(arr1, arr2):
    result = []
    index = 0

    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1

    p1 = 0
    p2 = 0
    while p1 < len(arr1) or p2 < len(arr2):
        num1 = arr1[p1]
        num2 = arr2[p2]
        if num1 < num2:
            result.append(num1)
            p1 += 1
        elif num2 < num1:
            result.append(num2)
            p2 += 1
        else:
            result[index] = num1

    return result


print(merge_sorted_array([0, 3, 4, 31], [4, 6, 30]))
