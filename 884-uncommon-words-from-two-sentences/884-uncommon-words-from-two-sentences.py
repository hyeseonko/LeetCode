class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words1= s1.split(" ")
        words2 = s2.split(" ")
        filtered_words1= [word for word in words1 if words1.count(word)==1]
        filtered_words2= [word for word in words2 if words2.count(word)==1]
        o1 = [word for word in filtered_words1 if word not in words2]
        o2 = [word for word in filtered_words2 if word not in words1]
        return o1+o2