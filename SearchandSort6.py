def merge_sorted_arrays(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    merged = [0] * (n1 + n2)
    i = 0
    j = 0
    k = 0


    while i < n1 and j < n2:
        if arr1[i] <= arr2[j]:
            merged[k] = arr1[i]
            i += 1
        else:
            merged[k] = arr2[j]
            j += 1
        k += 1


    while i < n1:
        merged[k] = arr1[i]
        i += 1
        k += 1


    while j < n2:
        merged[k] = arr2[j]
        j += 1
        k += 1

    return merged

# Test the function with example arrays
arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]

print(merge_sorted_arrays(arr1, arr2))
