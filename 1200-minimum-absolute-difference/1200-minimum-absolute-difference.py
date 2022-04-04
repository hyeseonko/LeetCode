class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        sarr = sorted(arr)
        minval = sarr[1]-sarr[0]
        output=[[sarr[0], sarr[1]]]
        for i in range(2, len(arr)):
            if sarr[i]-sarr[i-1] < minval:
                minval = sarr[i]-sarr[i-1]
                output = [[sarr[i-1], sarr[i]]]
            elif sarr[i]-sarr[i-1]==minval:
                output.append([sarr[i-1], sarr[i]])
        return output