class Solution:
    def calPoints(self, ops: List[str]) -> int:
        output = []
        for op in ops:
            if op=="C":
                output.pop(-1)
            elif op=="D":
                output.append(output[-1]*2)
            elif op=="+":
                output.append(output[-1]+output[-2])
            else:
                output.append(int(op))
        return sum(output)