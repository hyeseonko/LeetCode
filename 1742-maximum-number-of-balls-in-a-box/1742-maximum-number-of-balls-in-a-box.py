class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = [0]*50
        for ball in range(lowLimit, highLimit+1):
            count = sum([int(each) for each in str(ball)])
            boxes[count]+=1
        return max(boxes)