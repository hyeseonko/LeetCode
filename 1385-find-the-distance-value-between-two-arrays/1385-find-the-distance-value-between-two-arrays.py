class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        output = 0
        for arr in arr1:
            skip=True
            for a in arr2:
                if abs(arr-a)<=d:
                    skip=False
                    break
            if skip:
                output+=1
        return output