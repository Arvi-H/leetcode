# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

class ContainsDuplicate(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))

    # In terms of time complexity, both approaches have the same O(n) time complexity 
    # because they both iterate over each element of the input vector at most once. 
    # However, the approach of adding elements one by one to the set and checking for 
    # duplicates after each insertion might be more efficient in some scenarios because 
    # it can potentially stop early as soon as a duplicate is found, while the second 
    # approach must check every element in the input vector even if a duplicate is found early.

    def containsDuplicateEfficientSolution(self, nums):
        unique_nums = set()
        for i in nums:
            if i in unique_nums:
                return True
            unique_nums.add(i)        
        return False