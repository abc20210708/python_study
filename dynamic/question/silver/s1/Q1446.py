## 지름길 (실버 1)
#  참고 블로그 https://imzzan.tistory.com/m/221?t_src=GNBlayer_kakaostory

n, d = map(int,input().split())
n_list = [list(map(int,input().split())) for _ in range(n)]
graph = [i for i in range(d+1)]

for i in range(d+1):
	graph[i] = min(graph[i],graph[i-1]+1)
	for start,end,le in n_list:
		if i == start and end <= d:
			graph[end] = min(graph[end],graph[i]+le) 

print(graph[-1])