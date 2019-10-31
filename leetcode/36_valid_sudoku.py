from collections import defaultdict

SUB_N = 3
N = 9


class Solution:
    def isValidSudoku(self, board):
        # validate the lines
        for i in range(N):
            count = defaultdict(lambda: 0)
            for j in range(N):
                digit = board[i][j]
                if digit == '.':
                    continue
                count[digit] += 1
                if count[digit] > 1:
                    return False
            
        # validate the columns
        for j in range(N):
            count = defaultdict(lambda: 0)
            for i in range(N):
                digit = board[i][j]
                if digit == '.':
                    continue
                count[digit] += 1
                if count[digit] > 1:
                    return False
                
        # validate the sub boxes
        for start_i in range(SUB_N):
            for start_j in range(SUB_N):
                count = defaultdict(lambda: 0)
                for i in range(SUB_N):
                    for j in range(SUB_N):
                        i_, j_ = start_i*SUB_N + i, start_j*SUB_N + j
                        digit = board[i_][j_]
                        if digit == '.':
                            continue
                        count[digit] += 1
                        if count[digit] > 1:
                            return False
                        
        return True


if __name__ == '__main__':
    s = Solution()
    assert s.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]) == True
    assert s.isValidSudoku([["8","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]) == False
    