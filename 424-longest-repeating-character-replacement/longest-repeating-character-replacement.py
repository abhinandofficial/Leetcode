class Solution(object):
        def characterReplacement(self, s, k):
            res = 0
            l = 0
            map = {}
            for r in range(len(s)):
                map[s[r]] = 1 + map.get(s[r],0)
                if ((r-l+1)-max(map.values())) > k:
                    map[s[l]] -=1
                    l+=1
                res = max(res,r-l+1)
            return res

                
        