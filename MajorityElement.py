class Solution(object):
    def majorityElement(self, nums):
        frequencyMap = {}

        for i in nums:  
            if i in frequencyMap:
                frequencyMap[i] += 1
            else:
                frequencyMap[i] = 1

        maxFrequency =  max(frequencyMap, key=frequencyMap.get) 
        return maxFrequency