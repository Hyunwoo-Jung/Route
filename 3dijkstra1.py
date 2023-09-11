# 데이크스트라 알고리즘 : 선택할 정점을 고려해 효율적으로 최단 경로를 찾을 수 있음

def dijkstra(edges, num_v):
    dist = [float('inf')] * num_v
    dist[0] = 0
    q = [i for i in range(num_v)]

    while len(q) > 0: 
        # 가장 비용이 적은 정점 찾기
        r = q[0]
        for i in q:
            if dist[i] < dist[r]:
                r = i # 비용이 적은 정점이 발견되면 갱신
        
        # 가장 비용이 적은 정점을 꺼내기
        u = q.pop(q.index(r))
        for i in edges[u]: # 꺼낸 정점의 변을 반복
            if dist[i[0]] > dist[u] + i[1]:
                # 정점까지의 비용을 갱신할 수 있다면 갱신하기
                dist[i[0]] = dist[u] + i[1]
    return dist

# 변의 리스트(끝점과 비용의 리스트)
edges = [
    [[1, 4], [2, 3]], # 정점 A부터의 변 리스트
    [[2, 1], [3, 1], [4, 5]], # 정점 B부터의 변 리스트
    [[5, 2]], # 정점 C부터의 변 리스트
    [[4, 3]], # 정점 D부터의 변 리스트
    [[6, 2]], # 정점 E부터의 변 리스트
    [[4, 1], [6, 4]], # 정점 F부터의 변 리스트
    [] # 정점 G부터의 변 리스트
]

print(dijkstra(edges, 7))