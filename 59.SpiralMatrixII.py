class Solution:

    def digit(self, n):
        for value in range(1, n ** 2 + 1):
            yield value

    def generateMatrix(self, n: int) -> list[list[int]]:
        d = self.digit(n)
        if n == 1:
            k = 1
        elif n == 2:
            k = 1
        elif n == 3:
            k = 2
        else:
            k = n - 2
        lst = [[None for _ in range(n)] for _ in range(n)]

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
print(*a.generateMatrix(10), sep='\n')
