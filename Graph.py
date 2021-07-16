from collections import *

class Graph:
    
    def __init__(self, vertex = 0 ):
        self.g = defaultdict(list)
        self.n = vertex
        
    def create(self, edge_list = None):
        for edge in edge_list:
            self.g[edge[0]].append(edge[1])
        self.n = len(self.g)
    
    def dfs(self):
        res = []
        visited = [False for i in range(self.n)]
        def helper(x):
            res.append(x)
            visited[x] = True
            for i in self.g[x]:
                if not visited[i]:
                    helper(i)
        for i in range(self.n):
            if not visited[i]:
                helper(i)
        return res
    
    def bfs(self):
        res = []
        visited = [False for i in range(self.n)]
        queue = deque()
        for i in range(self.n):
            if not visited[i]:
                queue.append(x)
                visited[x] = True
                res.append(x)
                
                while queue:
                    x = queue.popleft()
                    for i in self.g:
                        if not visited[i]:
                            visited[i] = True
                            queue.append(i)
                            res.append(i)
    
        return res
    
    def iscyclic(self):
        visited = [False for i in range(self.n)]
        rec = [False for i in range(self.n)]
        def dfs(x):
            visited[x] = True
            rec[x] = True
            for i in self.g[x]:
                if not visited[i]:
                    if dfs(i): return False
                elif rec[i]: return True
            rec[x] = False
        for i in self.g[x]:
            if not visited[i]:
                if dfs(i):return True
        return False
    
    def get_toposort(self):
        visited = [False for i in range(self.n)]
        res = []
        def dfs(x):
            visited[x] = True
            for i in self.g[x]:
                if not visited[i]:
                    dfs(i)
            res.insert(0,x)
            
        for i in self.g[x]:
            if not visited[i]:
                dfs(i)
        return res
    
    def get_connected_compouned(self):
        visited = [False for i in range(self.n)]
        res = 0
        def dfs(x):
            visited[x] = True
            for i in self.g[x]:
                if not visited[i]:
                    dfs(i)
            
        for i in self.g[x]:
            if not visited[i]:
                res += 1
                dfs(i)
        return res
    
    def isBipartite(self):
        visited = [0 for i in range(self.n)]
        def dfs(x, color):
            visited[x] = color
            for i in self.g[x]:
                if not visited[i]:
                    if dfs(i, 3-color): return True
                elif rec[i] == rec[x]: return True
    
        for i in self.g[x]:
            if not visited[i]:
                if dfs(i, 1):
                    return False
        return True