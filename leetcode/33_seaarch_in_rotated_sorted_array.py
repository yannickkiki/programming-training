class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        
        n = len(nums)
        
        if n == 1:
            return 0 if target == nums[0] else -1
        
        left, right = 0, n-1
        while left < right:
            if right-left == 1:
                if nums[left]==target:
                    return left
                elif nums[right]==target:
                    return right
                else:
                    return -1  
            idx = (left+right)//2
            if nums[idx] > nums[left]:
                if nums[idx] >= target >= nums[left]:
                    right = idx
                else:
                    left = idx
            else:
                if nums[idx] <= target <= nums[right]:
                    left = idx
                else:
                    right = idx
                    

if __name__ == '__main__':
    s = Solution()
    assert s.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert s.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert s.search([4, 5, 6, 7, 0, 1, 2, 3], 3) == 7
    assert s.search([4, 5, 6, 7, 0, 1, 2, 3], 8) == -1
    assert s.search([1], 1) == 0
    assert s.search([1, 3], 2) == -1
