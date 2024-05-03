class Solution:
    def reverse(self, x: int) -> int:
        result = None
        if x == 0:
            return 0
        else:
            str_digit = str(x)
            if str_digit[0] == '-':
                result = int(str_digit[1:][::-1].rstrip('0')) * -1
            else:
                result = int(str_digit[::-1].rstrip('0'))
        if result < -2**31 or result > (2**31) - 1:
            return 0
        else:
            return result