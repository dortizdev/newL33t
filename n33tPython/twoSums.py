class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}

        for i,j in enumerate(nums):
            diff = target - j
            if diff in previous:
                return [previous[diff], i]
            previous[j] = i