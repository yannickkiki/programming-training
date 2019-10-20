class Solution:
    def maximizeSweetness(self, sweetness, K):
        left, right = 1, sum(sweetness)//(K+1)
        while left<right:
            value, n_cuts, current_cumul = (left+right+1)//2, 0, 0
            for chunk_sweetness in sweetness:
                current_cumul += chunk_sweetness
                if current_cumul >= value:
                    n_cuts += 1
                    current_cumul = 0
            n_cuts -= 1
            if n_cuts<K:
                right = value-1
            else:
                left = value
        return right

if __name__=='__main__':
    s = Solution()
    result = s.maximizeSweetness([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
    result = s.maximizeSweetness([1, 2, 2, 1, 2, 2, 1, 2, 2], 2)
    result = s.maximizeSweetness([87506,32090,9852,96263, 52415,67669,10703,27,98672,48664], 1)
