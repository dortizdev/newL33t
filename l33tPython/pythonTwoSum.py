class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbersList = {}
        
        for i, j in enumerate(nums):
            num = target - j
            if num in numbersList:
                return [numbersList[num], i]
            numbersList[j] = i