class Solution(object):
    def isHappy(self, n):
        result = sum = 0
        seen =set()
        while(1):
            while(n>0):
                sum+=(n%10)**2
                n/=10
            if sum == 1:
                return True
            else:
                if sum in seen:
                    return False
                else:
                    seen.add(sum)
                    n = sum
                    sum = 0

    

        