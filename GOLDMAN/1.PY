def findSpecialProduct(inputArray):
    # Write your code here
    newArr = [None for _ in range(len(inputArray))]
    for i in range(len(inputArray)):
        prod = 1
        for j in range(len(inputArray)):
            if i != j:
                prod *= inputArray[j]
        newArr[i] = prod
    return newArr
print(findSpecialProduct([4,6,7]))
