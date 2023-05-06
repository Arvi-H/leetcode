# Given an integer n, return an array ans of length n + 1 
# such that for each i (0 <= i <= n), ans[i] is the number 
# of 1's in the binary representation of i.

class CountingBits(object):
    def countBits(self, n):
        count = [0]*(n+1)

        for i in range(1, n+1):
            count[i] = count[i // 2] + (i % 2)
        
        return count
