class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        prior = words[0]
        for word in words[1:]:
            for p, w in zip(prior, word):
                if p==w:
                    continue
                elif p!=w and order.index(p)>order.index(w):
                    return False
                else:
                    break
            if len(prior)>len(word) and prior[:len(word)]==word:
                return False
            prior = word
        return True