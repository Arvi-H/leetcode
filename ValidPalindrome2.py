import re

class Solution(object):
    def validPalindrome(self, s):
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        
        left = 0
        right = len(s)-1
        
        while left < right:
            if s[left] != s[right]:
                one_deleted_left = s[left+1:right+1]
                one_deleted_right = s[left:right]  
                return one_deleted_left == one_deleted_left[::-1] or one_deleted_right == one_deleted_right[::-1]  
            
            # Increment
            left += 1
            right -= 1
            
        return True

sol = Solution()

# Test case: "abca"
result = sol.validPalindrome("deifggied")
print(result)  
