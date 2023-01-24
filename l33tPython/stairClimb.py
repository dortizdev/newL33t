class Solution:
    def climbStairs(self, n: int) -> int:
        firstStep, secondStep = 1, 1

        for i in range(n-1):
            temp = firstStep
            firstStep = firstStep + secondStep
            secondStep = temp

        return firstStep