class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        output=[]
        prev=0
        for num in target:
            output+=["Push", "Pop"]*(num-prev-1)
            output+=["Push"]
            prev=num
        return output