class Solution(object):
    def romanToInt(self, s):
        result=0
        roman = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        for x in range(len(s)):
            if(x+1 < len(s) and roman[s[x+1]] > roman[s[x]]):
                result -= roman[s[x]]
            else:
                result += roman[s[x]]
        return result