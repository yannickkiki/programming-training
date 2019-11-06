class Solution:
    def removeElement(self, nums, val):
        n_removed, i, n =  0, 0, len(nums)
        while i < n-n_removed:
            if nums[i] == val:
                del nums[i]
                n_removed += 1
            else:
                i += 1
        return n-n_removed
    

if __name__=='__main__':
    s = Solution()
    nums = [3, 2 ,2,3]
    assert s.removeElement(nums, 3) == 2
    assert nums == [2, 2]
