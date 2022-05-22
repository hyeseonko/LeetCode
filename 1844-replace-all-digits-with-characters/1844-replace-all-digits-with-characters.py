import string

class Solution:
    def replaceDigits(self, s: str) -> str:
        letter_count = dict((letter, i) for i, letter in enumerate(string.ascii_lowercase))
        count_letter = dict((i, letter) for i, letter in enumerate(string.ascii_lowercase))
        output=""
        for i, c in enumerate(s):
            if i%2==1:
                output+=count_letter[letter_count[s[i-1]]+int(c)]
            else:
                output+=c
        return output