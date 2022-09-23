class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # make a dictionary
        chars_dict = dict()
        for ch in chars:
            if ch not in chars_dict:
                chars_dict[ch]=0
            chars_dict[ch]+=1
        
        # verify each word
        output = 0
        for word in words:
            wordset = set(word)
            included = True
            for w in wordset:
                if w not in chars_dict:
                    included=False
                    break
                elif word.count(w)>chars_dict[w]:
                    included=False
                    break
                else:
                    continue
            if included:
                output+=len(word)
        return output
                    