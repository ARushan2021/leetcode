from itertools import permutations


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        return ''.join(map(str, [val for val in permutations(range(1, n+1))][k-1]))