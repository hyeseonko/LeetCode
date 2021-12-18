class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        basis = words[0]
        output=[]
        word_list=[list(word) for word in words[1:]]
        for s in basis:
            contained=True
            for word in word_list:
                if s not in word:
                    contained=False
                    break
            if contained:
                for w in word_list:
                    w.remove(s)
                output.append(s)
        return output