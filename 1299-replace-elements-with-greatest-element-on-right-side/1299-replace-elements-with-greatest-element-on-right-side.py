class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        output=[]
        for i, val in enumerate(arr[:-1]):
            output.append(max(arr[(i+1):]))
        output.append(-1)
        return output