import re

class Solution(object):
    def validPalindrome(self, s):
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        
        left = 0
        right = len(s)-1
        
        while left < right:
            if s[left] != s[right]:
                deleteLeftChar = s[left+1:right+1] 
                deleteRightChar = s[left:right]  
                return deleteLeftChar == deleteLeftChar[::-1] or deleteRightChar == deleteRightChar[::-1]  
            
            # Increment
            left += 1
            right -= 1
            
        return True

sol = Solution()

# Test case: "abca"
result = sol.validPalindrome("aaaaba")
print(result)  
