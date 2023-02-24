class Solution:
    def isHappy(self, n: int) -> bool:
        squaredSums = set()

        if n == 1:
            return True

        while n not in squaredSums:
            squaredSums.add(n)
            n = self.squareDigit(n)

            if n == 1:
                return True

        return False

    def squareDigit(self, n: int) -> int:
        value = 0

        while n:
            onesDigit = n % 10
            onesDigit = onesDigit ** 2
            value += onesDigit
            n = n // 10

        return value