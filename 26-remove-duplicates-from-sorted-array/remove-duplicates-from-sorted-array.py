class Solution(object):
    def removeDuplicates(self, nums):
        unique = -1
        for i in range(len(nums)):
            if  unique == -1 or nums[i]!=nums[unique]:
                    unique = unique +1 
                    nums[unique] = nums[i]
        return unique+1

        




     
        