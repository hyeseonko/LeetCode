class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        rev1 = num1[::-1]
        rev2 = num2[::-1]
        output1, output2 = 0, 0
        pow10 = 1
        for rv in rev1:
            output1 += int(rv)*pow10
            pow10 *= 10
        pow10 = 1
        for rv in rev2:
            output2 += int(rv)*pow10
            pow10 *= 10
        return str(output1+output2)