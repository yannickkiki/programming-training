from math import ceil

def find_median(nums1, nums2):
    total_len = len(nums1)+len(nums2)
    n = ceil(total_len/2)
    
    if len(nums1)>len(nums2):
        nums1, nums2 = nums2, nums1
        
    median = 0
    
    if len(nums1)==0:
        median = nums2[total_len//2]
        if total_len%2==0:
            median = (nums2[-1+total_len//2]+median)/2
        return median

    n1, n2 = 0, n
    if nums2[n2-1] <= nums1[n1]:
        median = nums2[n2-1]
        if total_len%2==0:
            if n2 < len(nums2):
                median = (min(nums1[n1], nums2[n2]) + median)/2
            else:
                median = (nums1[n1] + median)/2
        return median
    
    n1 = len(nums1)
    n2 = n-n1
    if nums1[n1-1] <= nums2[n2]:
        if n2>=1:
            median = max(nums1[n1-1], nums2[n2-1])
        else:
            median = nums1[n1-1]
        if total_len%2 == 0:
            median = (nums2[n2]+median)/2
        return median
    
    median, is_max_1, n1_min, n1_max = 0, True, 0, len(nums1)
    
    while True:
        n1 = (n1_min+n1_max)//2
        n2 = n-n1
        is_max_1 = nums1[n1-1] >= nums2[n2-1]
        if (nums2[n2-1] <= nums1[n1-1] <= nums2[n2]) or (nums1[n1-1] <= nums2[n2-1] <= nums1[n1]):
            median = max(nums1[n1-1], nums2[n2-1])
            if total_len%2==0:
                median = (min(nums1[n1], nums2[n2])+median)/2
            return median
        else:
            if is_max_1:
                n1_max = n1
            else:
                n1_min = n1

if __name__=='__main__':
    assert find_median([4, 20, 32, 50, 55, 61, 62], [1, 15, 22, 30, 70]) == 31
