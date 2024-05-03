class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        nums.append(target)
        nums.sort()
        return nums.index(target)