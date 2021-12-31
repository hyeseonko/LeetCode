class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[cost[0], cost[1]] # dp:= stepped on ith step
        for val in cost[2:]:
            dp.append(val+min(dp[-1], dp[-2]))
        return min(dp[-1],dp[-2])