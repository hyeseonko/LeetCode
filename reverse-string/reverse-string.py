class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid = int(len(s)/2)
        for i in range(1,mid+1):
            temp=s[mid+i+len(s)%2-1]
            s[mid+i+len(s)%2-1]=s[mid-i]
            s[mid-i]=temp