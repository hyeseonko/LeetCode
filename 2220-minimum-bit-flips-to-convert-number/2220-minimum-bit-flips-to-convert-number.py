class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        startbin="{0:b}".format(start)
        goalbin="{0:b}".format(goal)
        return sum([1 if s!=g else 0 for s, g in zip_longest(startbin[::-1], goalbin[::-1], fillvalue='0')])