class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] not in '([{':
            return False
        res = []
        for i in s:
            if i == '[':
                res.append(']')
            elif i == '(':
                res.append(')')
            elif i == '{':
                res.append('}')
            elif i in '])}':
                if len(res) == 0 or i != res.pop():
                    return False
        if len(res) == 0:
            return True
        else:
            return False