class Solution:
    def interpret(self, command: str) -> str:
        output =""
        cur = 0
        while(cur<len(command)):
            if command[cur]=="G":
                output+="G"
                cur+=1
            elif command[cur+1]==")":
                output+="o"
                cur+=2
            else:
                output+="al"
                cur+=4
        return output