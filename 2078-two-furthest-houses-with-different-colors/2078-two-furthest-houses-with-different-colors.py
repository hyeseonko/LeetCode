class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        
        # using the fact there are at least two different colors
        base = colors[0]
        output = 0
        for right in range(len(colors)-1, 0, -1):
            if colors[right]!=base:
                output = right
                break
                
        base = colors[-1]
        for left in range(len(colors)-1):
            if colors[left]!=base:
                return max(len(colors)-1-left, output)