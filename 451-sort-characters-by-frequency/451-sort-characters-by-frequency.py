class Solution:
    def frequencySort(self, s: str) -> str:
        set_letter = set(s)
        output = dict()
        for letter in set(s):
            output[letter]=s.count(letter)
        soutput = sorted(output.items(), key=lambda x: x[1], reverse=True)
        return "".join(s*c for s, c in soutput)