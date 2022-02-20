class Solution:
    def reverseWords(self, s: str) -> str:
        output=""
        for word in s.split(" "):
            output+="".join(word[-i] for i in range(1, len(word)+1))
            output+=" "
        return output.strip()