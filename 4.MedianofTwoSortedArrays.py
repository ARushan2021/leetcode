class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_array = sorted(nums1+nums2)
        if len(merged_array) % 2 != 0:
            ind = int(len(merged_array) / 2)
            result = merged_array[ind]
        elif len(merged_array) % 2 == 0:
            ind = int(len(merged_array) / 2)
            result = (merged_array[ind] + merged_array[ind-1])/2
        return float(result)