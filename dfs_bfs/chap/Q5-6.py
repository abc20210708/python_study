
# 인접 리스트 방식 예제
# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph1 = [[] for _ in range(3)]

#  노트 0에 연결되 노드 정보 저장(노드, 거리)
graph1[0].append((1,7))
graph1[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph1[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph1[2].append((0, 5))

print(graph1)