class Solution:
    def largestGoodInteger(self, num: str) -> str:
        output = [""]
        for i in range(len(num)-2):
            if len(set(num[i:i+3]))==1:
                output.append(num[i:i+3])
        return sorted(output)[-1]
            