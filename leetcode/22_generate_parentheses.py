class Solution:
    def generateParenthesis(self, n):
        result = list()
        def f(combination, n_open, n_closed):
            if n_open == n_closed == n:
                result.append(combination)
            else:
                if n_open < n:
                    f(combination + '(', n_open+1, n_closed)
                if n_open > n_closed:
                    f(combination + ')', n_open, n_closed+1)
    
        f("", 0, 0)
        return result

if __name__ == '__main__':
    s = Solution()
    result = s.generateParenthesis(3)
