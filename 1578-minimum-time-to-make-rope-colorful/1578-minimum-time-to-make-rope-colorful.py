class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        # Greedy
        output = 0
        same_color_pool = []
        for i in range(1, len(colors)):
            if colors[i]==colors[i-1]:
                if not same_color_pool:
                    same_color_pool.append(neededTime[i-1]) 
                same_color_pool.append(neededTime[i])
            else:
                if same_color_pool:
                    same_color_pool.sort()
                    output+=sum(same_color_pool[:-1])
                    same_color_pool=[]
        if same_color_pool:
            same_color_pool.sort()
            output+=sum(same_color_pool[:-1])
        return output