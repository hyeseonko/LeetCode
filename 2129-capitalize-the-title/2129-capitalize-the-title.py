class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.lower().split(" ")
        output=""
        for word in words:
            character = list(word)
            if len(word)>2:
                character[0]=character[0].upper()
            output+="".join(character)
            output+=" "
        return output.strip()