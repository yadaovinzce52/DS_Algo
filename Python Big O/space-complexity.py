def boo(n):
    for _ in range(len(n)):
        print("boo!")

boo([1,2,3,4,5,1,421,21,41,42124])

# O(1) space

def newFunc(n):
    array = []
    for element in n:
        array.append(element)

    return array

print(newFunc([1,5,1243,42,12,54154,214,312]))

# O(n) space complexity