class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        base = [(cost[0], 1) if cost[0]<cost[1] else (cost[1], -1) for cost in costs]
        basesum, balanced = 0, 0
        for v, b in base:
            basesum += v
            balanced += b
        pass_over = balanced//2
        if pass_over==0:
            diff = 0
        elif pass_over>0:
            diff = sum(sorted([abs(a-b) for a, b in costs if (a-b)<0])[:abs(pass_over)])
        else:
            diff = sum(sorted([abs(a-b) for a, b in costs if (a-b)>=0])[:abs(pass_over)])
        return basesum+diff