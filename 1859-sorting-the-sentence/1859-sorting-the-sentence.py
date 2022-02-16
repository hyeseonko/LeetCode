class Solution:
    def sortSentence(self, s: str) -> str:
        output=[(each[:-1], int(each[-1])) for each in s.split(" ")]
        sorted_output=sorted(output, key=lambda x:x[1])
        return " ".join(w for w,o in sorted_output)