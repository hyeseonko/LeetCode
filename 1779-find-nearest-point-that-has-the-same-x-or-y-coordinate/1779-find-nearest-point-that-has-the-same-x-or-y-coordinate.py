class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        candidates = []
        for i, point in enumerate(points):
            if point[0]==x or point[1]==y:
                candidates.append((abs(x-point[0])+abs(y-point[1]), i))
        candidates.sort()
        return candidates[0][1] if candidates else -1