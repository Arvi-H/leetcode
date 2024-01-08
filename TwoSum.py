class Solution(object):
    def twoSum(self, nums, target): #Input: nums = [3,2,4], target = 6
        myMap = {}

        for i in range(len(nums)):
            complement = target - nums[i] # complement = 3, nums[i] = 3, i = 0

            # search if what we need has been seen
            if complement in myMap:
                return i, myMap[complement]

            # if no complement found, store this number (nums[i]) for later reference
            myMap[nums[i]] = i  # 0, 3 -> index, complement

# Example input
nums = [3, 2, 4]
target = 6g

print("Indices of the two numbers:", Solution().twoSum(nums, target))