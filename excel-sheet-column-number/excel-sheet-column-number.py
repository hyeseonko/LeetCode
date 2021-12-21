class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        import string
        alphabet = dict((key, i+1) for i, key in enumerate(string.ascii_uppercase))
        mul={0:1}
        for i in range(1,8):
            mul[i]=mul[i-1]*26

        # Base 26 calculation
        output=0
        
        for i in range(len(columnTitle)):
            output+=alphabet[columnTitle[-i-1]]*mul[i]

        return output