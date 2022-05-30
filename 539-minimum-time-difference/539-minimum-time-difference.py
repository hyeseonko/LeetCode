class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        output = 1440 # maximum minutes (24-hours)
        first_h, first_m = timePoints[0].split(":")
        prev = 60*int(first_h)+int(first_m)
        for timePoint in timePoints[1:]:
            h, m = timePoint.split(":")            
            current = 60*int(h)+int(m)
            if current-prev < output:
                output = current-prev
            prev = current
        current = 60*int(first_h)+int(first_m)+1440
        if current-prev < output:
            output = current-prev
        return output