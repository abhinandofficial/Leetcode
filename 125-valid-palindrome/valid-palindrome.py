class Solution(object):
    def isPalindrome(self, s):
       s = "".join(char for char in s if char.isalnum())
        
       s = s.lower()
       right = len(s) -1
       for i in range(len(s)):
            if s[i] !=  s[right]:
                return False
            right = right -1
       return True
       
        