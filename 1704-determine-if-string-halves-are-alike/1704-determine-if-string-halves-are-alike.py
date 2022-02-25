class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        first = s[:int(len(s)/2)] 
        second = s[int(len(s)/2):]
        firstsum = sum([1 for f in first if f in vowel])
        secondsum = sum([1 for s in second if s in vowel])
        if firstsum==secondsum:
            return True
        else:
            return False