class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        check=[0,0,0,0]
        prev = None
        for p in password:
            if prev and p==prev:
                return False
            if p.isdigit():
                check[0]=1
            elif p in "!@#$%^&*()-+":
                check[1]=1
            elif p.islower():
                check[2]=1
            elif p.isupper():
                check[3]=1
            prev = p
        return True if sum(check)==4 else False