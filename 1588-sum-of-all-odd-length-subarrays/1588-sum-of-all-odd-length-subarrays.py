class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result=0
        N = len(arr)
        for i, val in enumerate(arr):
            result+=int(((i+1)*(N-i)+((i+1)%2)*(N%2))/2)*val
        return result