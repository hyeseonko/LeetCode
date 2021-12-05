class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        print(x[0])
        for i in range(int(len(x)/2)):
            if x[i]!=x[-i-1]:
                return False
        return True
        