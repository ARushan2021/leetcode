class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digit = str(int(''.join(map(str, digits))) + 1)
        return [int(i) for i in new_digit]