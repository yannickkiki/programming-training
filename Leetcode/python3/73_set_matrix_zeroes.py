class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        matrix[0][0] = (matrix[0][0], False, False)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 or (i==0 and j==0 and matrix[i][j][0]==0):
                    matrix[0][j] = 0 if j!=0 else (0, True, matrix[0][0][2])
                    # print(j, matrix[0][0])
                    matrix[i][0] = 0 if i!=0 else (0, matrix[0][0][1], True)
        
        # print(matrix)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                    
        if matrix[0][0][1]:
            for i in range(1, m):
                matrix[i][0] = 0
        if matrix[0][0][2]:
            for j in range(1, n):
                matrix[0][j] = 0
        matrix[0][0] = matrix[0][0][0]
    

if __name__ == '__main__':
    s = Solution()
    
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    s.setZeroes(matrix)
    assert matrix == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    s.setZeroes(matrix)
    assert matrix == [[1,0,1],[0,0,0],[1,0,1]]
    
    
    
    matrix = [[1,1,1],[0,1,2]]
    s.setZeroes(matrix)
    assert matrix == [[0,1,1],[0,0,0]]
    
    matrix = [[1,0,3]]
    s.setZeroes(matrix)
    assert matrix == [[0,0,0]]
