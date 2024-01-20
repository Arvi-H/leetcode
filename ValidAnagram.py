class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        trackSLetters = {}
        trackTLetters = {}
        
        for i in s:
            if i in trackSLetters:
                trackSLetters[i] += 1
            else:
                trackSLetters[i] = 1
        
        for i in t:
            if i in trackTLetters:
                trackTLetters[i] += 1
            else:
                trackTLetters[i] = 1

        for i in trackSLetters:
            if trackSLetters[i] != trackTLetters.get(i, 0):
                return False
            
        return True
         
solution = Solution()
result = solution.isAnagram("abdsba", "abdsbb")
print(result)