nums1 = [1, 3, 4, 6]
nums2 = [2, 5, 7, 8]

nums1 = [1, 3]
nums2 = [2]

total_len = len(nums1)+len(nums2)
idx1, idx2, median, end = 0, 0, 0, 1 + total_len//2

for idx in range(end):
    inferior_is_1 = True

    if idx1 == len(nums1):
        idx2 += 1
        inferior_is_1 = False
    elif idx2 == len(nums2):
        idx1 += 1
    else:
        if nums1[idx1] < nums2[idx2]:
            idx1 += 1
        else:
            idx2 += 1
            inferior_is_1 = False

    if total_len % 2 == 0:
        if idx == -1+(total_len//2):
            median += nums1[-1+idx1] if inferior_is_1 else nums2[-1+idx2]
        if idx == total_len//2:
            median += nums1[-1+idx1] if inferior_is_1 else nums2[-1+idx2]
            median /= 2
            

    if total_len % 2 == 1 and idx == total_len//2:
        median = nums1[-1+idx1] if inferior_is_1 else nums2[-1+idx2]
