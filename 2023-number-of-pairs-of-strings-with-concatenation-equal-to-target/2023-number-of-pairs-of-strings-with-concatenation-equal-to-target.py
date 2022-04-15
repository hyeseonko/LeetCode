class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        output=0
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i!=j and num1+num2==target:
                    output+=1
        return output