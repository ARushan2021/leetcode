class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        for _ in range(nums.count(val)):
            nums.remove(val)
        return len(nums)