class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard=["qwertyuiop", "asdfghjkl","zxcvbnm"]
        output=[]
        for word in words:
            w = word.lower()
            for key in keyboard:
                if w[0] in key:
                    where = key
            check=True
            
            for c in w[1:]:
                if c not in where:
                    check=False
                    break
            if check:
                output.append(word)
        return output                
            