# Solve using Floyd's Cycle Detection Algorithm (Tortoise and Hare)
class Solution(object):
    def isHappy(self, n):
        trackElements = set()
        
        while n not in trackElements:
            trackElements.add(n)
            
            n = self.squareNum(self, n)
            
            if n == 1:
                return True
        
        return False
        
    def squareNum(self, n):
       return sum(int(i)**2 for i in str(n))