class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sWord, tWord = {}, {}

        for i in range(len(s)):
            sWord[s[i]] = 1 + sWord.get(s[i],0)
            tWord[t[i]] = 1 + tWord.get(t[i],0)

        if sWord == tWord:
            return True
            
        return False