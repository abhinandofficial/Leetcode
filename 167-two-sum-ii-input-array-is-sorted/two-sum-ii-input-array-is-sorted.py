class Solution(object):
    def twoSum(self, numbers, target):
        right = len(numbers)-1
        left = 0
        while(left < right):
            if (numbers[left]+numbers[right] == target):
                return left +1 ,right+1
            elif (numbers[left]+numbers[right] < target):
                left = left +1
            elif (numbers[right]+numbers[left]>target):
                right = right -1
