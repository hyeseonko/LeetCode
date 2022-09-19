class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        output = []
        for i in range(len(rowSum)):
            cur =[]
            for j in range(len(colSum)):
                val = min(rowSum[i], colSum[j])
                cur.append(val)
                rowSum[i]-=val
                colSum[j]-=val
            output.append(cur)
        return output