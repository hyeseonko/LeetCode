class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        else:
            output=[[1], [1,1]]
            for i in range(numRows-2):
                dp=[1]
                for idx in range(len(output[-1])-1):
                    dp.append(output[-1][idx]+output[-1][idx+1])
                dp.append(1)                    
                output.append(dp)
            return output