class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        codes = dict()
        for m, a in zip(morse, string.ascii_lowercase):
            codes[a]=m
        
        result = set()
        for word in words:
            cur = ""
            for c in word:
                cur+=codes[c]
            result.add(cur)
        return len(result)