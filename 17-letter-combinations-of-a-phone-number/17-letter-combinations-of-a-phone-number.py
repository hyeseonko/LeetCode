class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        di = {"2": "abc", "3": "def", "4":"ghi", "5": "jkl", "6": "mno", "7":"pqrs","8":"tuv", "9":"wxyz"}
        if digits=="":
            return []
        output = [alph for alph in di[digits[0]]]
        # 23
        for digit in digits[1:]:
            cur = []
            while(output):
                target = output.pop(0)
                for alph in di[digit]:
                    cur.append(target+alph)
            output.extend(cur)
                    
        return output