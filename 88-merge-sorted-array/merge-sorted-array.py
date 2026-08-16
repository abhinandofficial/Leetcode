class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for j in range(n):
            nums1[j+m] = nums2[j]
        nums1.sort()
        return nums1
     
        