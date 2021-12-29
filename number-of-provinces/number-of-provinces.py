class Solution:
    def bfs(self, node: int) -> None:
        stack=[node]
        self.visited[node]=True
        while(stack):
            cur_node = stack.pop(0)
            for i in range(self.n):
                if not self.visited[i] and self.isConnected[cur_node][i]==1:
                    stack.append(i)
                    self.visited[i]=True
            
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.isConnected=isConnected
        self.n = len(isConnected)
        self.visited=[False for _ in range(self.n)]
        output=0
        for x in range(self.n):
            if self.visited[x]:
                continue 
            self.visited[x]=True
            output+=1
            for y in range(self.n):
                if not self.visited[y] and self.isConnected[x][y]==1:
                    self.bfs(y)
        return output