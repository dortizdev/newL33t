class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters = set()
        palLength = 0

        for i in s:
            if i in letters:
                letters.remove(i)
                palLength += 2
            else:
                letters.add(i)
        
        if len(letters) > 0:
            palLength += 1
        
        return palLength