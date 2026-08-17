class Solution(object):
    def lengthOfLastWord(self, s):
     counter = 0
     leng= len(s)-1
     for x in range(leng,-1,-1):
        if(s[x] != ' '):
            counter = counter + 1
        elif(counter > 0):
            return counter

     return counter
    



        