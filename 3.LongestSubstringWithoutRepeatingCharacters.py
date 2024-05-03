class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = []
        res = ''
        for i in range(len(s)):
            res = s[i]
            for j in s[1+i:]:
                if j not in res:
                    res += j
                elif j in res:
                    lst.append(len(res))
                    break
            lst.append(len(res))
        if len(lst) == 0:
            return 0
        else:
            return max(lst)