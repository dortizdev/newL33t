class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numList = set()
        for i in nums:
            if i not in numList:
                numList.add(i)
            elif i in numList:
                return True
            else:
                return False