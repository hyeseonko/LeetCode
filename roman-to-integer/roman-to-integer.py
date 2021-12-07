class Solution:
    def romanToInt(self, s: str) -> int:
        roman2int={"I":1, "V": 5, "X": 10, "L": 50, "C":100, "D": 500, "M":1000}
        output = 0
        cur_int = roman2int[s[0]]
        for next_str in s[1:]:
            if cur_int>=roman2int[next_str]:
                output+=cur_int
            else:
                output-=cur_int
            cur_int=roman2int[next_str]
        output+=roman2int[s[-1]]
        return output
        