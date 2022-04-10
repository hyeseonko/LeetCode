class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(set(s))==1:
            return s
        N=len(s)
        if s[0]==s[1]:
            output=[s[0], s[1]]
        else:
            output=[s[0]]
        for i in range(1, N-1):
            if 2*N-2*i-1<len(output):
                break
            cur=[s[i]]
            for j in range(1, min(i, N-i-1)+1):
                if s[i-j]==s[i+j]:
                    cur.insert(0, s[i-j])
                    cur.append(s[i+j])
                else:
                    break
            # when check by even
            if s[i]==s[i+1]:
                cur2=[s[i],s[i+1]]
                for j in range(1, min(i, N-i-2)+1):
                    if s[i-j]==s[i+1+j]:
                        cur2.insert(0, s[i-j])
                        cur2.append(s[i+1+j])
                    else:
                        break
                if len(output)<len(cur2):
                    output=cur2
            if len(output)<len(cur):
                output = cur
        return "".join(output)