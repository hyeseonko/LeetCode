class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping = dict()
        i=0
        for k in key.replace(" ",""):
            if k not in mapping:
                mapping[k]=string.ascii_lowercase[i]
                i+=1
        output = ""
        for m in message:
            if m==" ":
                output+=" "
            else:
                output+=mapping[m]
        return output