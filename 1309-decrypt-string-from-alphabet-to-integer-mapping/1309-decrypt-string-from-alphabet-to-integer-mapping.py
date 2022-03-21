import string
class Solution:
    def freqAlphabets(self, s: str) -> str:
        di = dict(zip(range(1, 27), string.ascii_lowercase))
        output=""
        slist = s.split("#")
        for numstr in slist[:-1]:
            output+="".join([di[int(n)] for n in numstr[:-2]])
            output+=di[int(numstr[-2:])]
        output+="".join([di[int(n)] for n in slist[-1]])
        return output