# LEETCODE


# class Solution:
#     def rotate(self, nums, k):
#         n = len(nums)
#         k = k % n
#         nums[:] = nums[-k:] + nums[:-k]


def rotate(nums, k):
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]
    return nums


# Example usage
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Original:", arr)
print("Rotated :", rotate(arr, k))


# OUTPUT:
# Original: [1, 2, 3, 4, 5, 6, 7]
# Rotated : [5, 6, 7, 1, 2, 3, 4]