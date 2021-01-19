from math import ceil

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                for j in range(i+1, n):
                    if nums[j] <= nums[i]:
                        nums[i], nums[j-1] = nums[j-1], nums[i]
                        nums[i+1:n] = nums[n-1:i:-1]
                        return
                nums[i], nums[-1] = nums[-1], nums[i]
                nums[i+1:n] = nums[n-1:i:-1]
                return
        nums[:] = nums[::-1]


if __name__ == '__main__':
    s = Solution()
    nums1 = [1, 2, 3]
    s.nextPermutation(nums1) #1-3-2
    nums2 = [3, 2, 1]
    s.nextPermutation(nums2)# 1-2-3
    nums3 = [1, 1, 5]
    s.nextPermutation(nums3)# 1-5-1
    nums4 = [4, 4, 2, 1]
    s.nextPermutation(nums4)#1-2-4-4
    nums5 = [1, 3, 2]
    s.nextPermutation(nums5)#2-1-3
    nums6 = [8, 9, 7]
    s.nextPermutation(nums6)#9-7-8
    nums7 = [1, 5, 1]
    s.nextPermutation(nums7) #5-1-1
