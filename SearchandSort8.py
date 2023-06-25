def intersection(nums1, nums2):
    freq = {}
    for num in nums1:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1

    intersection = []
    for num in nums2:
        if num in freq and freq[num] > 0:
            intersection.append(num)
            freq[num] -= 1

    return intersection

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

print(intersection(nums1, nums2))
