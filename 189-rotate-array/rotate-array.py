class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        nums.reverse()
        l,r = 0,k-1
        while(l<r):
            nums[l],nums[r] = nums[r],nums[l]
            l = l+1
            r = r-1
        l,r = k,len(nums)-1
        while(l<r):
            nums[l],nums[r] = nums[r],nums[l]
            l = l+1
            r = r-1
       

        