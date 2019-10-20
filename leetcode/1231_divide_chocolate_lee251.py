class Solution:
    def maximizeSweetness(self, A, K):
        left, right = 1, sum(A) // (K + 1)
        while left < right:
            mid = (left + right + 1) // 2
            cur = cuts = 0
            for a in A:
                cur += a
                if cur >= mid:
                    cuts += 1
                    cur = 0
            if cuts > K:
                left = mid
            else:
                right = mid - 1
        return right

if __name__=='__main__':
    s = Solution()
    result = s.maximizeSweetness([87506,32090,9852,96263, 52415,67669,10703,27,98672,48664], 1)
    