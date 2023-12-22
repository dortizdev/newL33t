class Solution:
    def hammingWeight(self, n: int) -> int:
        ones = 0

        while n is not 0:
            ones += n % 2
            n = n >> 1

        return ones