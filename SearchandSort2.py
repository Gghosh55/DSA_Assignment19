def countSmaller(nums):
    def mergeSort(arr, indices):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = mergeSort(arr[:mid], indices[:mid])
        right = mergeSort(arr[mid:], indices[mid:])
        return merge(left, right)

    def merge(left, right):
        merged = []
        count = 0
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                counts[left[i][1]] += count
                merged.append(left[i])
                i += 1
            else:
                count += 1
                merged.append(right[j])
                j += 1

        while i < len(left):
            counts[left[i][1]] += count
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged

    counts = [0] * len(nums)
    nums_with_indices = [(nums[i], i) for i in range(len(nums))]
    mergeSort(nums_with_indices, counts)

    return counts
nums = [5, 2, 6, 1]
print(countSmaller(nums))
