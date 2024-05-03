class Solution:
    def myAtoi(self, s: str) -> int:
        s_substring = ''
        votriclovo = False
        str_digit = ''
        digit = None
        s = s.lstrip()
        if s == '':
            return 0
        if s[0] == '-':
            votriclovo = True
            s_substring = s[1:]
        elif s[0] == '+':
            s_substring = s[1:]
        else:
            s_substring = s
        for i in s_substring:
            if i.isdigit():
                str_digit += i
            else:
                break
        if str_digit == '':
            return 0
        else:
            if votriclovo is True:
                digit = int(str_digit) * -1
            else:
                digit = int(str_digit)
        if digit <= -2**31:
            return -2**31
        elif digit >= (2**31) - 1:
            return (2**31) - 1
        else:
            return digit