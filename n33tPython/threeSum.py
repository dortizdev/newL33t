class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()

        if len(nums) < 3:
            return answer

        for i,j in enumerate(nums):
            if i > 0 and j == nums[i - 1]:
                continue

            l,r = i + 1, len(nums) - 1
            while l < r:
                currSum = j + nums[l] + nums[r]
                if currSum > 0:
                    r = r - 1
                elif currSum < 0:
                    l = l + 1
                else:
                    answer.append([j, nums[l], nums[r]])
                    l = l + 1
                    while nums[l] == nums[l - 1] and l < r:
                        l = l + 1
        return answer