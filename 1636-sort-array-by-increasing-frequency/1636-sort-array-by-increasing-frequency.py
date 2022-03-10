class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        numfreq=dict()
        for num in nums:
            if num not in numfreq:
                numfreq[num]=0
            numfreq[num]+=1
        snum = sorted(numfreq.items(), key=lambda x: (x[1], -x[0]), reverse=False)
        output=[]
        for k, v in snum:
            output+=[k]*v
        return output