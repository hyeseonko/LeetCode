class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq=dict()
        for num in arr:
            if num not in freq:
                freq[num]=0
            freq[num]+=1
        
        occurences = [v for _, v in freq.items()]
        if len(occurences)==len(set(occurences)):
            return True
        else:
            return False
            