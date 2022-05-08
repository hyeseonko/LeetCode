class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        dp=[1, 1]
        for i, pkey in enumerate(pressedKeys[1:], 1):
            temp=dp[-1]
            if i>=1 and pressedKeys[i-1]==pkey:
                temp+=dp[-2]
                if i>=2 and pressedKeys[i-2]==pkey:
                    temp+=dp[-3]
                    if i>=3 and pkey in {"7", "9"} and pressedKeys[i-3]==pkey:
                        temp+=dp[-4]
            dp.append(temp)
        return dp[-1]%1000000007