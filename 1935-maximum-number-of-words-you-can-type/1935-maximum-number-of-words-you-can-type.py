class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        output = 0
        for word in text.split(" "):
            skip=False
            for letter in brokenLetters:
                if letter in word:
                    skip=True
                    break
            if not skip:
                output+=1
        return output
            