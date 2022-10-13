class Solution:
    def greatestLetter(self, s: str) -> str:
        alphabet=set()
        result = []
        for c in s:
            if c.isupper() and c.lower() in alphabet:
                result.append(string.ascii_uppercase.index(c))
            elif c.islower() and c.upper() in alphabet:
                result.append(string.ascii_uppercase.index(c.upper()))
            alphabet.add(c)
        return string.ascii_uppercase[sorted(result)[-1]] if result else ""
        
        