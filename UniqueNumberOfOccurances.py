class Solution(object):
    def uniqueOccurrences(self, arr):
        trackOccurences = {}
        
        for i in range(len(arr)):
            if arr[i] in trackOccurences:
                trackOccurences[arr[i]] += 1
            else:                
                trackOccurences[arr[i]] = 1
                
        return len(trackOccurences.values()) == len(set(trackOccurences.values()))

solution = Solution()
test_case = [1, 2, 2, 1, 1, 3]
result = solution.uniqueOccurrences(test_case)
print(result)