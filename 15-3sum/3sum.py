class Solution(object):
    def threeSum(self, nums):
        result = []
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and a == nums[i-1]:
                continue
            l = i +1
            r = len(nums)-1
            while(l<r):
                summ = a + nums[l] + nums[r]
                if summ>0:
                    r -=1
                elif summ<0:
                    l +=1
                else:
                    result.append([a,nums[l],nums[r]])
                    l+=1
                    while(l<r and nums[l] == nums[l-1]):
                        l+=1
        return result

                    

                    
                    