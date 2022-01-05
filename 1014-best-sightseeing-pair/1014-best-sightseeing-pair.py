class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        output = [-1]
        maxval = values[0]-1
        for value in values[1:]:
            output.append(maxval+value)
            maxval = value if value > maxval else maxval
            maxval-=1
        return max(output)