class Solution:
    def checkString(self, s: str) -> bool:
        a_indices = [i for i, x in enumerate(s) if x=='a']
        try:
            if a_indices[-1] > s.index('b'):
                return False
        except:
            pass
        return True

        