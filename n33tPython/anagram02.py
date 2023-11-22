class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagramS = {}
        anagramT = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            anagramS[s[i]] = 1 + anagramS.get(s[i], 0)
        for j in range(len(t)):
            anagramT[t[j]] = 1 + anagramT.get(t[j], 0)

        if anagramS == anagramT:
            return True
        else:
            return False