import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
            while '**' in p:
                p = p.replace('**', '*')
            res = re.fullmatch(p, s)
            if res is None:
                return False
            else:
                return True