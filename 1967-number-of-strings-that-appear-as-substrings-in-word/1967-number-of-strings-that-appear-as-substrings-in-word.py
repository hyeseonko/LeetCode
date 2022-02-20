class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        output=0
        for pattern in patterns:
            if pattern in word:
                output+=1
        return output
        