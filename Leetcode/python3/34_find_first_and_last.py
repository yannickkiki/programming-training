class Solution:
    def searchRange(self, nums, target):
        n = len(nums)
        
        if n==0:
            return [-1, -1]
        
        # find index of an element equal to target
        left, right = 0, n-1
        is_target_found, target_idx = False, 0
        if nums[right] == target:
            is_target_found = True
            target_idx = right
            
        while left < right:
            idx = (left+right)//2
            if nums[idx] < target:
                left = idx+1
            elif nums[idx] > target:
                right = idx
            else:
                is_target_found, target_idx = True, idx
                break

        if not is_target_found:
            return [-1, -1]
        
        # find first position of target
        left, right = 0, target_idx
        while left < right:
            idx = (left+right)//2
            if nums[idx] < target:
                left = idx+1
            else:
                right = idx
        first_idx = left
        
        # find last position of target
        left, right = target_idx, n-1
        if nums[right] == target:
            last_idx = right
        else:
            while left < right:
                idx = (left+right)//2
                if nums[idx] > target:
                    right = idx
                else:
                    left = idx+1
            last_idx = left-1
        
        return [first_idx, last_idx]
            

if __name__ == '__main__':
    s = Solution()
    result = s.searchRange([7], 8)
    assert s.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1] 
    assert s.searchRange([8, 8], 8) == [0, 1]
    assert s.searchRange([8], 8) == [0, 0]
