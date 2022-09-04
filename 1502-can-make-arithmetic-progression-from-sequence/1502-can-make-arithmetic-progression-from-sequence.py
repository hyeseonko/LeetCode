class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[1]-arr[0]
        prev = arr[1]
        for a in arr[2:]:
            if a-prev!=diff:
                return False
            prev=a
        return True