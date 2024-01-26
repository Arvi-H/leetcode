class Solution(object):
    def removeDuplicates(self, nums):
        nums = set(nums)
        return len(nums)  
        
print(Solution().removeDuplicates([1,2,3,3,5])) 