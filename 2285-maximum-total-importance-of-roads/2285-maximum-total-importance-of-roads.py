class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        path=[0]*n
        for road in roads:
            path[road[0]]+=1
            path[road[1]]+=1
        path.sort()
        return sum([each*i for i, each in enumerate(path, 1)])