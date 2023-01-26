class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numberList = {}
        
        for i in nums:
            if i not in numberList:
                numberList[i] = 1
            else:
                numberList[i] += 1
        
            if numberList[i] > len(nums)/2:
                
                return i