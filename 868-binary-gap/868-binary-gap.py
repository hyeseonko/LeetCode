class Solution:
    def binaryGap(self, n: int) -> int:
        # convert integer to binary
        binary_n = str("{0:b}".format(n))
        start = 0
        diff = 0
        for i, each in enumerate(binary_n[1:]):
            if each=="1":
                if i+1-start > diff:
                    diff = i+1-start
                start = i+1
        return diff