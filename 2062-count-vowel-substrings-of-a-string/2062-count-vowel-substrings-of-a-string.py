class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        total = 0
        for i in range(len(word)):
            cur_word = word[i:]
            vowel = {"a":0, "e": 0, "i":0, "o": 0, "u":0} # reset
            if word[i] not in vowel:
                continue
            for w in cur_word:
                if w in vowel:
                    vowel[w]=1
                    if all(value == 1 for value in vowel.values()):
                        total += 1
                else:
                    break
        return total