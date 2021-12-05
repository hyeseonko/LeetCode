class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        # 1. list of integers --> list of strings
        str_digits = [str(d) for d in digits]
        # 2. plus one and then convert it to string
        str_digits=str(int("".join(str_digits))+1)
        # 3. add items into list
        output=[int(d) for d in str_digits]

        return output
        
        
        