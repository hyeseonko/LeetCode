class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        filtered_words=[word for word in words1 if words1.count(word)==1]
        return sum([1 for word in filtered_words if words2.count(word)==1])
        