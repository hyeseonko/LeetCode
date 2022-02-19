class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        snum = sorted(nums)
        _max = snum.pop(0)+snum.pop(-1)
        while(snum):
            cur = snum.pop(0)+snum.pop(-1)
            if cur>_max:
                _max = cur
        return _max
        