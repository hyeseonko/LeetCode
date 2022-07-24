class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_count = dict()
        for num in nums:
            if num not in num_count:
                num_count[num]=0
            num_count[num]+=1
        if len(num_count.keys())<2: return 0
        prev_k, prev_v = 1000000001, 0
        output = 0
        for k in sorted(num_count):
            if k-prev_k==1 and output<prev_v+num_count[k]:
                output = prev_v + num_count[k]
            prev_k, prev_v = k, num_count[k]
        return output
            
                