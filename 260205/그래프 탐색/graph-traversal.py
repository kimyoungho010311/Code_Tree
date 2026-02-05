
n, m = tuple(map(int, input().split()))

# index를 1번부터 사용하기 위해 n+1만큼 배열을 선언한다.
graph = [[] for _ in range(n+1)]

visited = [False for _ in range(n+1)]
vertex_cnt = 0

def dfs(vertex):
    global  vertex_cnt

    # 해당 정점에서 이어져 있는 모든 정점을 탐색한다.
    for curr_v in graph[vertex]:
        # 아직 간선이 존재하고 방문한 적이 없는 정점에 대해서만 탐색을 진행
        if not visited[curr_v]:
            visited[curr_v] = True
            vertex_cnt += 1
            dfs(curr_v)



for i in range(m):
    v1, v2 = tuple(map(int, input().split()))

    graph[v1].append(v2)
    graph[v2].append(v1)

visited[1] = True
dfs(1)

print(vertex_cnt)