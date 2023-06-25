def arrange_alternate(arr):
    n = len(arr)
    posPtr = 0
    negPtr = 0

    # Find the first positive number and negative number
    while posPtr < n and arr[posPtr] < 0:
        posPtr += 1
    while negPtr < n and arr[negPtr] >= 0:
        negPtr += 1

    # Arrange positive and negative numbers alternately
    while posPtr < n and negPtr < n:
        # Swap positive and negative numbers
        arr[posPtr], arr[negPtr] = arr[negPtr], arr[posPtr]

        # Move the pointers to the next positive and negative numbers
        posPtr += 1
        negPtr += 1

        # Find the next positive number and negative number
        while posPtr < n and arr[posPtr] < 0:
            posPtr += 1
        while negPtr < n and arr[negPtr] >= 0:
            negPtr += 1

    return arr

# Test the function with the given examples
arr1 = [1, 2, 3, -4, -1, 4]
arr2 = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]

print(arrange_alternate(arr1))
print(arrange_alternate(arr2))
