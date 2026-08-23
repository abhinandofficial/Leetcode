class Solution(object):
    def containsDuplicate(self, nums):
        has = set()

        for num in nums:
            if num in has:
                return True
            has.add(num)

        return False