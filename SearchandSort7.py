def intersection(nums1, nums2):
    set1 = set(nums1)
    intersection = set()

    for num in nums2:
        if num in set1:
            intersection.add(num)

    return list(intersection)

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(intersection(nums1, nums2))
