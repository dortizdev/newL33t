class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        integer = 0

        for i in nums:
            integer = i ^ integer

        return integer