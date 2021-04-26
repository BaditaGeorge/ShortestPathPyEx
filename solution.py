class Solution:
    def __init__(self):
        self.distances = dict()
        self.graph = dict()

    def clearInMemoryData(self):
        self.distances = dict()
        self.graph = dict()

    def findShortestPath(self,A,B):
        q = [A]
        self.distances[A] = 0
        while q:
            head = q.pop(0)
            for neighbor in self.graph[head]:
                if neighbor not in self.distances:
                    self.distances[neighbor] = self.distances[head] + 1
                    q.append(neighbor)
                    if neighbor == B:
                        return self.distances[neighbor]
        return -1


    def find_intersection(self,distancesF,distancesB):
        ans = -1
        for i in self.graph:
            if i in distancesB and i in distancesF:
                if ans == -1:
                    ans = distancesF[i] +  distancesB[i]
                else:
                    ans = min(ans,distancesF[i]+distancesB[i])
        return ans

    def findShortestPath_bidirectional(self,A,B):
        qForward = [A]
        qBackward = [B]
        if A not in self.graph or B not in self.graph:
            return -1
        distancesForward = dict()
        distancesBackward = dict()
        distancesForward[A] = 0
        distancesBackward[B] = 0
        while qForward and qBackward:
            head = qForward.pop(0)
            back = qBackward.pop(0)
            if head in distancesBackward or back in distancesForward:
                return self.find_intersection(distancesForward, distancesBackward)
            for neighbor in self.graph[head]:
                if neighbor not in distancesForward:
                    distancesForward[neighbor] = distancesForward[head] + 1
                    qForward.append(neighbor)
            for neighbor in self.graph[back]:
                if neighbor not in distancesBackward:
                    distancesBackward[neighbor] = distancesBackward[back] + 1
                    qBackward.append(neighbor)
        return -1

    def readInput(self,path):
        reader = open(path,'r')
        line = reader.readline()
        while line:
            [friendA,friendB] = line.strip().split(' ')
            if friendA not in self.graph:
                self.graph[friendA] = set()
            if friendB not in self.graph:
                self.graph[friendB] = set()
            self.graph[friendA].add(friendB)
            self.graph[friendB].add(friendA)
            line = reader.readline()

    def solve(self):
        self.readInput('./data2.txt')
        print(self.findShortestPath('D', 'T'))
        print(self.findShortestPath_bidirectional('D','J'))


sol = Solution()
sol.solve()

# 1. Social network is represented as a undirected graph. 2. I chose this way to represend the network because it is the closest
# abstraction to what a social network means, having this concept of nodes that are point of interest, like users in a social network
# and edges that are relationship between users(two users represents two nodes, and nodes are connected if users have a friendship relation).
# 3. Algorithm that I used is BFS(breadth first search). Another alternatives could be DFS/Bellman Ford/Dijkstra's Algorithm.
# Dijkstra and Bellman-Ford are usefull for problems where our graph has costs attached to its edges, in this case we want minimum
# cost of a path between two nodes and this means that minimum cost path is not necessarly the one that contains the minimum number
# of edges. For our problem, Dijkstra and Bellman-Ford are not the best solution in our case because they have time complexity greater
# than BFS/DFS and are way to complex for what our problem means. Between BFS and DFS, i chose BFS because DFS has problems in 
# finding shortest path in a cyclic graph, this problem can be solved by checking if we minimize an already computed
# distance, for a node already visited and if we do so, continuing exploration for that node and minimizing distances for its
# neighbors. Anyway, this solution is still polynomyal but slower than a BFS and implementation is more complicated.
# I've created two test case scenarios
# First one, which is a big cyclic graph, and this is important because it shows that algorithm it's not affected by cycles and 
# reaches the target on the shortest path through its searching strategy (Exploring all neighbors of a give node).
# Second test case combines a cycle with a line graph, with few connections to the cycle graph and it shows in a more clearly manner
# that algorithm will always pick the shortest path, because it's the first/fastest way to reach the target node.
# A secondary implementation is a Bi-direcitonal BFS, it has same performances with the BFS on the most cases, but for
# some graphs that have a structure that is for example, wider in the proximity of the target and goal node and is a bit narrower
# in the section between this two nodes, that would be an example where this bi-directional search offers a real improvement.