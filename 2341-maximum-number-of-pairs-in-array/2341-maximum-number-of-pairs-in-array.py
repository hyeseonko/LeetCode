class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        numdict = dict()
        for num in nums:
            if num not in numdict:
                numdict[num]=0
            numdict[num]+=1
        output = [0, 0]
        for k, v in numdict.items():
            output[0]+=(v//2)
            output[1]+=(v%2)
        return output
                