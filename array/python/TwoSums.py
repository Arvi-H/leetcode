# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class TwoSums(object):
    def twoSum(self, nums, target):
        twoSumMap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in twoSumMap:
                return [twoSumMap[complement], i]
            
            twoSumMap[nums[i]] = i

        return []
     
print(TwoSums().twoSum([2, 7, 11, 15], 9))