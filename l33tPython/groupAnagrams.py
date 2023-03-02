class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for i in strs:
            groups["".join(sorted(list(i)))].append(i)

        return groups.values()