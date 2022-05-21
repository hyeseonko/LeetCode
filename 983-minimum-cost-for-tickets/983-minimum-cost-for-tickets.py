class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp=[min(costs)]
        for day in days[1:]:
            cost1 = dp[-1] + costs[0]
            week = int(next(x for x, val in enumerate(days) if val >= day-6))
            mth = int(next(x for x, val in enumerate(days) if val >= day-29))
            cost2 = dp[week-1] + costs[1] if week>=1 else costs[1]
            cost3 = dp[mth-1] + costs[2] if mth>=1 else costs[2]
            dp.append(min(cost1, cost2, cost3))
        return dp[-1]