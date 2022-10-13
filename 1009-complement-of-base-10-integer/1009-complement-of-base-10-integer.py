class Solution:
    def bitwiseComplement(self, n: int) -> int:
        num_bin = "{0:b}".format(n)
        complement = ""
        for n in num_bin:
            if n=="1":
                complement+="0"
            else:
                complement+="1"
        return int(complement, 2)