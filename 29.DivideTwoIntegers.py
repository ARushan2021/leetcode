class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = int(dividend/divisor)
        if result <= -2147483648:
            return -2147483648
        elif result >= 2147483648:
            return 2147483647
        else:
            return result