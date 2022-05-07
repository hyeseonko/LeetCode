class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram=dict()
        for word in strs:
            wordkey=""
            for c in sorted(set(word)):
                wordkey+=c+str(word.count(c))
            if wordkey in anagram:
                anagram[wordkey].append(word)
            else:
                anagram[wordkey]=[word]
        return [item for item in anagram.values()]
                            