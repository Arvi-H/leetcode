import sys

class Solution(object):
    def maxProfit(self, prices):
        minPrice = sys.maxsize  
        maxProfit = 0

        for i in range(len(prices)): # [7,1,5,3,6,4] | [7,6,4,3,1]
            if prices[i] < minPrice:
                minPrice = prices[i]
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
        
        return maxProfit
    
prices = [7,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(prices)) # Output: 5