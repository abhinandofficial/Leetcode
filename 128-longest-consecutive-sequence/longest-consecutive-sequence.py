class Solution(object):
    def longestConsecutive(self, nums):
        hashset = set(nums)
        longest= 0

        for i in (hashset):
            if i-1 not in hashset:
                length = 0
                while(i + length) in hashset :
                    length+=1
                longest = max(longest,length)
        return longest
        