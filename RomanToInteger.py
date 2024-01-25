class Solution(object):
    def romanToInt(self, s):
        intValue = 0
        valueMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        # LVIII
        for i in s: 
                
            intValue += valueMap[i]
        
        return intValue
            
print(Solution().romanToInt("III"))