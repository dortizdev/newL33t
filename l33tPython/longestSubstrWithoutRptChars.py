class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l, total = 0, 0

        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            total = max(total, r - l + 1)
            
        return total