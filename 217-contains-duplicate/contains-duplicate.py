class Solution(object):
    def containsDuplicate(self, nums):
         has = set()
         for i in range(len(nums)):
                if nums[i] in has:
                    return True
                else:
                    has.add(nums[i])
         return False
        