class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        dp=[0]
        for each in gain:
            dp.append(dp[-1]+each)
        return max(dp)
        
