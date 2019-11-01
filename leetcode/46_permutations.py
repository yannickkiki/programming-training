class Solution:
    def permute(self, nums):
        def f(l):
            if len(l) == len(nums):
                result.append(l)
            for num in nums:
                if not is_num_used[num]:
                    is_num_used[num] = True
                    f(l+[num])
                    is_num_used[num] = False
            
        
        result = list()
        is_num_used = {num: False for num in nums}
        f([])
        return result
    

if __name__ == '__main__':
    s = Solution()
    assert sorted(s.permute([1, 2, 3])) == sorted([[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]])
    