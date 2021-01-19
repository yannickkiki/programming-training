class Solution:
    def removeDuplicates(self, nums):
        current, n_removed, i, n = None, 0, 0, len(nums)
        while i < n-n_removed:
            if nums[i] == current:
                del nums[i]
                n_removed += 1
            else:
                current = nums[i]
                i += 1
        return n-n_removed
    

if __name__=='__main__':
    s = Solution()
    nums = [1,1,2]
    assert s.removeDuplicates(nums) == 2
    assert nums == [1, 2]
    nums = [0,0,1,1,1,2,2,3,3,4]
    assert s.removeDuplicates(nums) == 5
    assert nums == [0, 1, 2, 3, 4]
