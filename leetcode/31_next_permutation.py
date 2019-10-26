from math import ceil

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        
        n = len(nums)
        is_permuted = False
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                is_permuted = True
                break
        if not is_permuted:
            end = ceil(n/2)
            for i in range(end):
                nums[i], nums[n-i-1] = nums[n-i-1], nums[i]
        """
   
    
if __name__ == '__main__':
    s = Solution()
    # nums = [1, 2, 3]
    # nums = [3, 2, 1]
    # nums = [1, 1, 5]
    # nums = [4, 4, 2, 1]
    nums = [1, 3, 2]
    result = s.nextPermutation(nums)
