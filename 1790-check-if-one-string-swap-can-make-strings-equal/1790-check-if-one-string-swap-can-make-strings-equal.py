class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1==s2:
            return True
        else:
            # I will give you one last chance
            diff=0
            for c1, c2 in zip(s1, s2):
                if c1!=c2:
                    if diff==0:
                        d1, d2 = c1, c2
                    elif diff==1:
                        if c1!=d2 or c2!=d1:
                            return False
                    else:
                        return False
                    diff+=1
            
            return True if diff%2==0 else False