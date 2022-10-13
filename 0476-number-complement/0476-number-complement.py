class Solution:
    def findComplement(self, num: int) -> int:
        num_bin = "{0:b}".format(num)
        complement = ""
        for n in num_bin:
            if n=="1":
                complement+="0"
            else:
                complement+="1"
        return int(complement, 2)