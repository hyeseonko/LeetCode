class Solution:
    def reverse(self, x: int) -> int:

        if x<0:
            target=str(x)[1:]
            reveresed = "".join(target[-i] for i in range(1,len(target)+1))
            output = (-1)*int(reveresed)
        else:
            target=str(x)
            reveresed = "".join(target[-i] for i in range(1,len(target)+1))
            output = int(reveresed)
            
        if output>2**31-1 or output<-(2**31):
            return 0
        return output

        