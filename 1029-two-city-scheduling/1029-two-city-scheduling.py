class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        base = [(cost[0], 1) if cost[0]<cost[1] else (cost[1], -1) for cost in costs]
        basesum = sum([v for v, _ in base])
        balanced = sum([b for _, b in base])       
        pass_over = balanced//2
        if pass_over==0:
            diff = 0
        elif pass_over>0:
            diff = sum(sorted([abs(a-b) for a, b in costs if (a-b)*pass_over<0])[:abs(pass_over)])
        else:
            diff = sum(sorted([abs(a-b) for a, b in costs if (a-b)>=0])[:abs(pass_over)])
        return basesum+diff