from queue import PriorityQueue
from pprint import pprint as pp

v = 14 
graph = [[] for i in range(v)]

def bestfirstsearch(src , target , n):
    visited = [False] * n 
    pq = PriorityQueue()
    pq.put((0,src))
    visited[src] = True
    while pq.empty() == False :
        u  = pq.get()[1]
        print(u)
        
        if u == target :
            break 
        for v,c in graph[u]:
            if visited[v] == False :
                visited[v] = True 
                pq.put((c,v))
    print()
    
def addedge(x,y,cost):
    graph[y].append((x,cost))
    graph[x].append((y,cost))
    
addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)

pp(graph)
source = 0
target = 9
bestfirstsearch(source, target, v)
 
 
/* OUTPUT 

[[(1, 3), (2, 6), (3, 5)],
 [(0, 3), (4, 9), (5, 8)],
 [(0, 6), (6, 12), (7, 14)],
 [(0, 5), (8, 7)],
 [(1, 9)],
 [(1, 8)],
 [(2, 12)],
 [(2, 14)],
 [(3, 7), (9, 5), (10, 6)],
 [(8, 5), (11, 1), (12, 10), (13, 2)],
 [(8, 6)],
 [(9, 1)],
 [(9, 10)],
 [(9, 2)]]
0
1
3
2
8
9
*/
