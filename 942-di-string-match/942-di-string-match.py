class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        numset = [_ for _ in range(len(s)+1)]
        output=[]
        for each in s:
            if each == "I":
                output.append(numset[0])
                numset.pop(0)
            else:
                output.append(numset[-1])
                numset.pop(-1)
        output.append(numset[0])
        return output