class Solution:
    def maxProduct(self, words: List[str]) -> int:
        output = 0  # save the maximum product of word lengths
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if set(words[i]).intersection(set(words[j])):
                    continue
                cur = len(words[i])*len(words[j])
                if cur>output:
                    output = cur
        return output