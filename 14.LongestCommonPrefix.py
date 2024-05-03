class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        short_str = sorted(strs, key=len)[0]
        while len(short_str) > 0:
            for word in strs:
                if short_str != word[:len(short_str)]:
                    short_str = short_str[:-1]
                    break
            else:
                return short_str
        return ''