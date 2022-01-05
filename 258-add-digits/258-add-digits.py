class Solution:
    def addDigits(self, num: int) -> int:
        output = [int(s) for s in str(num)]
        while(1):
            if len(output)==1:
                return sum(output)
            output = [int(s) for s in str(sum(output))]