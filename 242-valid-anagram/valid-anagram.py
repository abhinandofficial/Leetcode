class Solution(object):
    def isAnagram(self, s, t):
     has1 = {}
     has2 = {}
     if len(s) != len(t):
        return False
     for i in range(len(s)):
        has1[s[i]] = 1 + has1.get(s[i],0)
        has2[t[i]] = 1 + has2.get(t[i],0)
     return has1 == has2


