class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lens = len(s)
        numset = [_ for _ in range(lens+1)]
        output=[]
        left_pointer=0
        right_pointer=lens
        for each in s:
            if each == "I":
                output.append(numset[left_pointer])
                left_pointer+=1
            else:
                output.append(numset[right_pointer])
                right_pointer-=1
        output.append(numset[left_pointer])
        return output