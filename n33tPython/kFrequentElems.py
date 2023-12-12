class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        chars = {}
        amount = [[] for i in range(len(nums) + 1)]
        answer = []

        for n in nums:
            chars[n] = 1 + chars.get(n,0)
        for n, c in chars.items():
            amount[c].append(n)

        for i in range(len(amount) - 1, 0, -1):
            for n in amount[i]:
                answer.append(n)
                if len(answer) == k:
                    return answer