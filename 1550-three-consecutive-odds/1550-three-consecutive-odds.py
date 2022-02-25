class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        times=0
        for num in arr:
            if num%2==0:
                times=0
            else:
                if times==2:
                    return True
                times+=1
        return False