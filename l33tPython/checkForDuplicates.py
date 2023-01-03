class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        arrSet = set()
        
        for i in nums:
            if i in arrSet:
                return True
            arrSet.add(i)
        return False