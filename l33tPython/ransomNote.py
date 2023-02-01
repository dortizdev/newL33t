class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magSet = {}

        if len(ransomNote) > len(magazine):
            return False

        for i in magazine:
            if i not in magSet:
                magSet[i] = 1
            else:
                magSet[i] += 1

        for j in ransomNote:
            if j not in magSet or magSet[j] == 0:
                return False
            else:
                magSet[j] -= 1
        return True