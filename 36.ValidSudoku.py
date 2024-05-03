class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check_rows
        if self.check_valid(board) is False:
            return False
        # check_columns
        if self.check_valid(tuple(zip(*board))) is False:
            return False

        cells = [[],[],[],[],[],[],[],[],[]]
        for lst in board[0:3]:
            cells[0] += lst[:3]
            cells[1] += lst[3:6]
            cells[2] += lst[6:]
        for lst in board[3:6]:
            cells[3] += lst[:3]
            cells[4] += lst[3:6]
            cells[5] += lst[6:]
        for lst in board[6:]:
            cells[6] += lst[:3]
            cells[7] += lst[3:6]
            cells[8] += lst[6:]

        # check_cells
        if self.check_valid(cells) is False:
            return False
        return True

    # Проверка строк, все элементы цифры от 1 до 9, нет повторяющихся
    def check_valid(self, iter_with_iter):
        digits = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '.')
        for lst in iter_with_iter:
            for elem in lst:
                if elem not in digits:
                    return False
            lst_int = tuple(int(i) for i in lst if i in digits[:-1])
            if sum(lst_int) != sum(set(lst_int)):
                return False
        return True