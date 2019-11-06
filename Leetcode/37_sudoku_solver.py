from collections import defaultdict

SUB_N = 3
N = 9

def is_verified(i, j, board):
    count = defaultdict(lambda: 0)
    for j_ in range(0, N):
        digit = board[i][j_]
        if digit == '.':
            continue
        count[digit] += 1
        if count[digit] > 1:
            return False

    count = defaultdict(lambda: 0)
    for i_ in range(0, N):
        digit = board[i_][j]
        if digit == '.':
            continue
        count[digit] += 1
        if count[digit] > 1:
            return False

    count, start_i, start_j = defaultdict(lambda: 0), i-i%3, j-j%3
    for i_ in range(start_i, start_i+SUB_N):
        for j_ in range(start_j, start_j+SUB_N):
            digit = board[i_][j_]
            if digit == '.':
                continue
            count[digit] += 1
            if count[digit] > 1:
                return False
            
    return True
    
class Solution:
    def solveSudoku(self, board):
        empty_cells = list()
        for i in range(N):
            for j in range(N):
                if board[i][j] == '.':
                    empty_cells.append((i, j))
        
        def f(empty_cell_idx, board):
            if empty_cell_idx == len(empty_cells):
                return True
            
            i, j = empty_cells[empty_cell_idx]
            for val in range(1, N+1):
                board[i][j] = str(val)
                if is_verified(i, j, board) and f(empty_cell_idx+1, board):
                    return True
                board[i][j] = '.'

        f(0, board)
        

if __name__ == '__main__':
    s = Solution()
    board1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    s.solveSudoku(board1)
    solved_board1 = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
    assert board1 == solved_board1
