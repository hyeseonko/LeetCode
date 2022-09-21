# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 1, n
        while(1):
            cur = (start+end)//2
            ans = guess(cur)
            if ans == 0:
                return cur
            elif ans > 0:
                start = cur+1
            else:
                end = cur-1
        