class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        dct = {'1':None, '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        result = []
        if '1' in digits:
            digits = digits.replace('1', '')
        if digits == '':
            result = result
        elif len(digits) ==1:
            for i in dct[digits]:
                if i not in result:
                    result.append(i)
        elif len(digits) == 2:
            result = [i+j for i in dct[digits[0]] for j in dct[digits[1]]]
        elif len(digits) == 3:
            result = [i+j+l for i in dct[digits[0]] for j in dct[digits[1]] for l in dct[digits[2]]]
        elif len(digits) == 4:
            result = [i+j+l+k for i in dct[digits[0]] for j in dct[digits[1]] for l in dct[digits[2]] for k in dct[digits[3]]]
        return result