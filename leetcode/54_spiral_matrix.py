class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return list()
        step, result = 0, list()
        m, n = len(matrix), len(matrix[0])
        while True:
            count = 0
            for j in range(step, n-step):
                count += 1
                result.append(matrix[step][j])
            if count == 0:
                break
            
            count = 0
            for i in range(step+1, m-step):
                count += 1
                result.append(matrix[i][n-1-step])
            if count == 0:
                break
            
            count = 0
            for j in range(n-step-2, step-1, -1):
                count += 1
                result.append(matrix[m-1-step][j])
            if count == 0:
                break
            
            count = 0
            for i in range(m-2-step, step, -1):
                count += 1
                result.append(matrix[i][step])
            if count == 0:
                break
            
            step += 1
        return result


if __name__ == '__main__':
    s = Solution()
    assert s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert s.spiralOrder([[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
    assert s.spiralOrder([[1, 2, 3],[4, 5, 6], [7, 8, 9],[10,11,12]]) == [1,2,3,6,9,12,11,10,7,4,5,8]