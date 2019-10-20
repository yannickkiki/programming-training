class Solution:
    def maximizeSweetness(self, sweetness, K):
        left, right = 1, sum(sweetness)//(K+1)
        while True:
            value, n_cuts, current_cumul = (left+right+1)//2, 0, 0
            if value==right:
                value -= 1
            min_sweet = 10**10
            for chunk_sweetness in sweetness:
                current_cumul += chunk_sweetness
                if current_cumul >= value:
                    n_cuts += 1
                    min_sweet = min(current_cumul, min_sweet)
                    current_cumul = 0
            n_cuts -= 1
            if n_cuts==K:
                print(min_sweet)
                return max(value, min_sweet)
            elif n_cuts<K:
                right = value
            else:
                left = value

if __name__=='__main__':
    s = Solution()
    result = s.maximizeSweetness([87506,32090,9852,96263, 52415,67669,10703,27,98672,48664], 1)
