class Solution(object):
    def numRollsToTarget(self, n, k, target):
        MOD = 10**9 + 7
        dp_table = [0] * (target + 1)  
        dp_table[0] = 1

        for i in range(n):
            new_dp_table = [0] * (target + 1)

            for j in range(1, k + 1):
                
                for face in range(j, target + 1):
                    new_dp_table[face] = (new_dp_table[face] + dp_table[face - j]) % MOD
            
            dp_table = new_dp_table

        return dp_table[target]