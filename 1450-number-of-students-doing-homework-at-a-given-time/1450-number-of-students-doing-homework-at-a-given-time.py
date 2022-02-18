class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        num = 0
        for st, et in zip(startTime, endTime):
            if queryTime in range(st, et+1):
                num+=1
        return num