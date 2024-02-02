class Solution(object): 
    def smallerNumbersThanCurrent(self, nums):
        sortedNums = sorted(nums) # 1, 2, 2, 3, 8
        myMap = {}
        
        for i in range(len(sortedNums)):
            if sortedNums[i] not in myMap: 
                myMap[sortedNums[i]] = len(sortedNums[:i])
                
        return [myMap[num] for num in nums]           
        
print(Solution().smallerNumbersThanCurrent([1, 2, 2, 3, 8]))