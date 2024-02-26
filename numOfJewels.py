class Solution(object):
    def numJewelsInStones(self, jewels, stones): 
        numOfJewels = 0

        for stone in stones:
            if stone in jewels:
                numOfJewels += 1
                
        return numOfJewels