class Solution:
    def sumZero(self, n: int) -> List[int]:
        output=[i for i in range(1,int(n/2)+1)]
        output+=[-i for i in range(1,int(n/2)+1)]
        if n%2!=0:
            output+=[0]
        return output