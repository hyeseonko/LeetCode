class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            groups[''.join(sorted(word))].append(word)
        return list(groups.values())
