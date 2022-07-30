class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        # 1. create dictionary (hash table) with word2
        word_dict = dict()
        for word in words2:
            temp_dict=dict()
            for c in word:
                if c not in word_dict:
                    word_dict[c]=1
                if c not in temp_dict:
                    temp_dict[c]=0
                temp_dict[c]+=1
                word_dict[c]+=1 if temp_dict[c]>word_dict[c] else 0
        # 2. verify
        output=[]
        for word in words1:
            flag=True
            for k, v in word_dict.items():
                if word.count(k)<v:
                    flag=False
                    break
            if flag:
                output.append(word)
        return output