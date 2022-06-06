class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        alphabet = [c for c in string.ascii_uppercase]
        digit = [str(i) for i in range(1, 10)]
        from_row = alphabet.index(s[0])
        from_col = digit.index(s[1])
        to_row = alphabet.index(s[3])
        to_col = digit.index(s[4])
        output=[]
        for alpha in range(from_row, to_row+1):
            for di in range(from_col, to_col+1):
                output.append(alphabet[alpha]+digit[di])
        return output
        
        