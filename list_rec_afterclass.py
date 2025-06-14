def numarray(array):

    if not array:
       return 0
    return 1 + numarray(array[1:])

a = [1,2,3,4,5,6,7]

print("Value of array ", a)
print("\nLength of array ", numarray(a))