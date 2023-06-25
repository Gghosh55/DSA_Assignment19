def sortArray(nums):
    def mergeSort(nums, left, right):
        if left < right:
            mid = (left + right) // 2
            mergeSort(nums, left, mid)
            mergeSort(nums, mid + 1, right)
            merge(nums, left, mid, right)

    def merge(nums, left, mid, right):
        temp = [0] * (right - left + 1)
        i = left
        j = mid + 1
        k = 0

        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp[k] = nums[i]
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
            k += 1

        while i <= mid:
            temp[k] = nums[i]
            i += 1
            k += 1

        while j <= right:
            temp[k] = nums[j]
            j += 1
            k += 1


        for i in range(len(temp)):
            nums[left + i] = temp[i]

    mergeSort(nums, 0, len(nums) - 1)
    return nums

nums = [5, 2, 3, 1]
print(sortArray(nums))
