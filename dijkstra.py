#code
from math import inf
def shortest_path(g):
    g_len = len(g)
    shortest_dist = {}
    for i in range(2, g_len+1):
        shortest_dist[i] = inf
    shortest_dist[1] = 0
    sp_list = {1:0}
    cur = 1
    while(len(sp_list) < g_len):
        print(len(sp_list))
        new_min = inf
        new_cur = -1
        for adj in g[cur]:
            print(adj)
            if shortest_dist[cur] + 1 < shortest_dist[adj]:
                shortest_dist[adj] = shortest_dist[cur] + 1
            if shortest_dist[adj] < new_min:
                new_min = shortest_dist[adj]
                new_cur = adj
            sp_list[new_cur] = new_min
        cur = new_cur
    return sp_list[len(g)]

def main():
    t=int(input())
    for _ in range(t):
        print("This went through")
        n=int(input())
        edge={i:[] for i in range(1,n+1)}
        for i in range(1,n+1):
            x=i+1
            y=3*i
            if x<=n:
                edge[i].append(x)
            if y<=n:
                edge[i].append(y)
        print(shortest_path(edge))
main()