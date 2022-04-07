class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while(len(stones)>1):
            sorted_stones = sorted(stones)
            diff = sorted_stones[-1]-sorted_stones[-2]
            stones = sorted_stones[:-2]
            if diff!=0:
                stones.append(diff)
        return stones[0] if stones else 0