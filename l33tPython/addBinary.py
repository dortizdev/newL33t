class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        carryOver = 0

        a, b = list(a), list(b)

        while a or b or carryOver == 1:
            if a:
                carryOver += int(a.pop())
            if b:
                carryOver += int(b.pop())

            res += str(carryOver % 2)
            carryOver = carryOver // 2

        return res[::-1]