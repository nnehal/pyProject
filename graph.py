from collections import deque

# def add_edge(mat, i, j):
#     mat[i][j] = 1
#     mat[j][i] = 1

def add_edge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def display_adj_list(adj):
    print("Adjacency List Representation:")

    for i in range(len(adj)):
        print(f"{i}: ", end="")
        for j in adj[i]:
            print(j, end=" ")
        print()

def display_matrix(mat):
    for row in mat:
        print(" ".join(map(str, row)))

def bfs(adj, s):
    q = deque()

    visited = [False] * len(adj)
    visited[s] = True
    q.append(s)

    while q:
        curr = q.popleft()
        print(curr, end=" ")

        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

def dfs_rec(adj, visited, s):
    visited[s] = True

    print(s, end=" ")

    for i in adj[s]:
        if not visited[i]:
            dfs_rec(adj, visited, i)

def dfs(adj, s):
    visited = [False] * len(adj)

    dfs_rec(adj, visited, s)



def main():
    V = 5
    # mat = [[0] * Vertices for _ in range(Vertices)]

    adj = [[] for _ in range(V)]

    add_edge(adj, 1, 2)
    add_edge(adj, 1, 0)
    add_edge(adj, 2, 0)
    add_edge(adj, 2, 3)
    add_edge(adj, 2, 4)

    # add_edge(adj, 0, 1)
    # add_edge(adj, 0, 2)
    # add_edge(adj, 1, 2)
    # add_edge(adj, 2, 3)

    # display_matrix(mat)
    display_adj_list(adj)

    print("BFS Traversal starting from 0: ")
    bfs(adj, 0)
    print()

    print("DFS Traversal starting from 0: ")
    dfs(adj, 1)
    print()

if __name__ == "__main__":
    main()