class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(len(sent.split()) for sent in sentences)
        