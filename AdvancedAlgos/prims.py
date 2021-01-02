#User function Template for python3

# Function to construct and return cost of MST for a graph
# represented using adjacency matrix representation
'''
V: nodes in graph
E: number of edges in graph
graph: adjacency matrix, graph[i][j]=weight, if edge exits , else float("inf").
'''
def spanningTree(V, E, graph):
    #code here
    mst_cut = {0 : 0} 
    u = 0

    while(len(mst_cut)<V):
        min_weight = float("inf")
        new_u = -1
        for v in range(len(graph[u])):
            print(min_weight)
            if graph[u][v] < min_weight and mst_cut.get(v, -1) == -1:
                min_weight = graph[u][v]
                new_u = v
        mst_cut[new_u] = min_weight
        u = new_u
    mst_weight = 0
    for node, weight in mst_cut.items():
        mst_weight += weight
    return mst_weight

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        graph = [[float("inf") for i in range(V)] for i in range(V)]
        for i in range(0,len(info),3):
            u,v,w = info[i]-1,info[i+1]-1,info[i+2]
            graph[u][v] = w
            graph[v][u] = w
        print(spanningTree(V,E,graph))
# } Driver Code Ends