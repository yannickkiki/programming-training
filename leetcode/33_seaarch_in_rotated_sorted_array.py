class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        
        n = len(nums)
        left, first_item, right, last_item = 0, nums[0], n-1, nums[n-1]
        while left < right:
            idx = (left+right)//2
            print(left, right, idx)
            if nums[idx] > first_item:
                if nums[idx] > target > first_item:
                    right = idx
                else:
                    left = idx+1
            else:
                if nums[idx] < target < last_item:
                    left = idx+1
                else:
                    right = idx
        return left if target == nums[left] else -1
                    

if __name__ == '__main__':
    s = Solution()
    result = s.search([4,5,6,7,8,0,1,2,3], 1)
        