class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for first_term in nums:
            second_term = target - first_term
            if second_term in nums[nums.index(first_term)+1:]:
                first_index = nums.index(first_term)
                second_index = nums[nums.index(first_term)+1:].index(second_term) + first_index + 1
                return [first_index, second_index]