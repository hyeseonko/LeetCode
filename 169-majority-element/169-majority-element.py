class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        N = len(nums)
        uniq_Ns = set(nums[:int(N+1/2)])
        for n in uniq_Ns:
            if nums.count(n)>(N/2):
                return n