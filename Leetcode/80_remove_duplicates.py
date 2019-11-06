class Solution:
    def removeDuplicates(self, nums):
        current, count, n_removed, i, n = None, 0, 0, 0, len(nums)
        while i < n-n_removed:
            if nums[i] != current:
                current, count = nums[i], 1
                i += 1
            elif count==2:
                del nums[i]
                n_removed += 1
            else:
                count += 1
                i += 1
            
        return n-n_removed
    

if __name__=='__main__':
    s = Solution()
    nums = [1,1,1,2,2,3]
    assert s.removeDuplicates(nums) == 5
    assert nums == [1,1,2,2,3]
    
    nums = [0,0,1,1,1,1,2,3,3]
    assert s.removeDuplicates(nums) == 7
    assert nums == [0,0,1,1,2,3,3]
