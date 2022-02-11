class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([stones.count(jewel) for jewel in jewels])