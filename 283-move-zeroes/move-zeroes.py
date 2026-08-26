class Solution(object):
    def moveZeroes(self, nums):
        j=0
        for i in range(len(nums)):
                if nums[i]!=0:
                    nums[j] = nums[i]
                    j=j+1
        while j < len(nums):
            nums[j]=0
            j=j+1

             


               
       
            
