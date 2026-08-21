class Solution(object):
    def twoSum(self, nums, target):
        dicti={}
        for i,num in enumerate(nums):
            com = target-num
            if com in dicti:
                return i,dicti[com]
            dicti[num]=i