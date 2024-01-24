# Solve using Floyd's Cycle Detection Algorithm (Tortoise and Hare)
class Solution(object):
    def isHappy(self, n):
        trackElements = set()
        
        while n not in trackElements:
            trackElements.add(n)
            
            n = self.squareNum(n)
            
            if n == 1:
                return True
        
        return False
        
    def squareNum(self, n):
        sum = 0
       
        while n:
            digit = n % 10
            digit = digit ** 2
            sum += digit
            n = n // 10
            
        return sum 