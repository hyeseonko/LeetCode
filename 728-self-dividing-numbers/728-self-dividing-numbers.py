class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output=[]
        for num in range(left, right+1):
            flag=True
            if "0" in str(num):
                continue
            for c in str(num):
                if num%int(c)!=0:
                    flag=False
                    break
            if flag:
                output.append(num)
        return output