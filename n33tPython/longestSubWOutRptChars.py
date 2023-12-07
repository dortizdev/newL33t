class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word = set()
        j = 0
        final = 0

        for i in range(len(s)):
          while s[i] in word:
            word.remove(s[j])
            j += 1
          word.add(s[i])
          final = max(final, i - j + 1)
        return final