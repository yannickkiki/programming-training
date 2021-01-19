class Solution:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1]*n
        for idx in range(1, n):
            val = 1+candies[idx-1] if ratings[idx] > ratings[idx-1] else 1
            candies[idx] = max(candies[idx], val)
            
            idx_ = n-1-idx
            val = 1+candies[idx_+1] if ratings[idx_] > ratings[idx_+1] else 1
            candies[idx_] = max(candies[idx_], val)
        return sum(candies)
    

if __name__ == '__main__':
    s = Solution()
    assert s.candy([1,0,2]) == 5
    assert s.candy([1,2,2]) == 4
