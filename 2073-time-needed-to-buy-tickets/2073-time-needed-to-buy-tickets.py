class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        queue=[(0, ticket) if k!=i else (1, ticket) for i, ticket in enumerate(tickets)]
        times = 1
        while(queue):
            target, left = queue.pop(0)
            if target==1 and left==1:
                return times
            if left>1:
                queue.append((target, left-1))
            times+=1