# 프로그래머스 level3 섬 연결하기

def solution(n, costs):
    # 특정 원소가 속한 집합을 찾기
    def find_parent(parent, x):
        # 루트 노드를 찾을 때까지 재귀 호출
        if parent[x] != x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    # 두 원소가 속한 집합을 합치기
    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

    parent = [i for i in range(n)]
    edges = [(c, a, b) for a, b, c in costs]
    edges.sort()
    result = 0

    for edge in edges:
        cost, a, b = edge
        # 사이클이 발생하지 않는 경우에만 집합에 포함
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            result += cost

    return result


solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])