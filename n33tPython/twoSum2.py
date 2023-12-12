class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            answer = numbers[l] + numbers[r]

            if answer > target:
                r = r - 1
            elif answer < target:
                l = l + 1
            else:
                return [l + 1, r + 1]