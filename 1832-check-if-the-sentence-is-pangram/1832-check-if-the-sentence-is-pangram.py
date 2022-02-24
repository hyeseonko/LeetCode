import string

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = list(string.ascii_lowercase)
        for letter in letters:
            if letter not in sentence:
                return False
        return True