def pushZerosToEnd(nums):
    n = len(nums)
    leftmost_zero_index = 0

    for i in range(n):
        if nums[i] != 0:
            nums[i], nums[leftmost_zero_index] = nums[leftmost_zero_index], nums[i]
            leftmost_zero_index += 1

    return nums
nums = [1, 2, 0, 4, 3, 0, 5, 0]
print(pushZerosToEnd(nums))
