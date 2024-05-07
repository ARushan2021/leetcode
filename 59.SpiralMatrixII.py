class Solution:

    def digit(self, n):
        for value in range(1, n ** 2 + 1):
            yield value


    def generateMatrix(self, n: int) -> list[list[int]]:
        lst = [[None for _ in range(n)] for _ in range(n)]
        d = self.digit(n)
        k = 1 if n <= 2 else 2 if n == 3 else n - 2

        for x in range(k):
            for i in range(x, n-x):
                lst[x][i] = next(d)
            for i in range(x + 1, n-1-x):
                lst[i][-1-x] = next(d)
            for i in range(n-1-x, x, -1):
                lst[0-x-1][i] = next(d)
            for i in range(n-1-x, x, -1):
                lst[i][x] = next(d)

        return lst


a = Solution()
print(*a.generateMatrix(3), sep='\n')
