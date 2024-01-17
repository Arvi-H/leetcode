class Solution(object):
    def setZeroes(self, matrix):
        zeroSet = set()

        for i, row in enumerate(matrix):
            if 0 in row:
                zeroSet.update(index for index, value in enumerate(row) if value == 0)
                matrix[i] = [0] * len(row)

        for row in matrix:
            for index in zeroSet:
                row[index] = 0
                
# Test case
test_matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

solution = Solution()
solution.setZeroes(test_matrix)

# Print the formatted matrix
for row in test_matrix:
    print(row)