# 그래프 탐색

하나의 정점으로부터 시작하여 차례대로 모든 정점들을 한 번씩 방문하는 것

## 그래프

아이템(사물 또는 추상적 개념)들과 이들 사이의 연결 관계를 표현

정점(Vertex)들의 집합과 이들을 연결하는 간선(Edge)들의 집합으로 구성된 자료 구조

방향성: 정하기 나름

- 무향: 동등한 관계
- 유향: 동등하지 않은 관계. ex)  사랑의 짝대기, 대소관계

인접 정점(Adjacency)

- 두개의 정점에 간선이 존재하면 서로 인점해있음
- 간선을 표시하는 방법-> 정점을 저장하게 됨
- 정점이 N개이면 최대 N-1개의 인접 정점이 있을수 있음

인접 행렬 방식

- 행렬로 표현하는 방식

  ```python
  arr = [ #1 2, 1 4, 2 1, 2 3, 3 1, 4 1
  '0101',
  '1010',
  '0100',
  '1000',
  ]
  ```

- 직관적으로 보기좋음(방향성이 보임)

- 정점의 개수가 많아질수록 크기가 커지고, 접근할때도 많이 돌아야함

인접 리스트 방식

- 노드에 연결된 점들을 배열로 주는 것

  ```python
  #[1] -> 2, 4
  #[2] -> 1, 3
  #[3] -> 2
  #[4] -> 1
  arr = [1,2,1,4,2,1,2,3,3,2,4,1]
  ```

- 크기가 행렬방식에 비해 작음

- 단방향인지 양방향인지(방향성) 확인 필요



## 깊이 우선탐색 Depth First Search

시작 정점의 한 방향으로 탐색하다가 탐색할곳이 없어지면 **갈림길로 돌아가** 다시 탐색

- 마지막에 만났던 갈림길의 정점으로 돌아가야하므로 **스택** 필요
- 방문했는지 확인이 필요함

비선형인 그래프구조

- 그래프 표현된 **모든 자료를 빠짐없이 검색하는 것**이 중요. (백트래킹과 다른점)



알고리즘 순서

1. 시작 정점 v를 결정하여 방문한다
2. 정점 v에 인접한 정점 중에서
   1. 방문하지 않은 정점 w가 있으면 정점 v를 스택에 push하고 정점 w를 방문함. 그리고 w를 v로 하여 다시 2를 반복한다.
   2. 방문하지 않은 정점이 없으면 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2를 반복한다.
3. 스택이 공백이 될때까지 2를 반복한다.



```python
# pseudo code, recursive
# G: 그래프, v: 방문하려는 정점
def DFS_recursive(G, v, visited):
    visited[v] = True
    # v와인접한 모든 w에 대해서
    for each all w in adjacency(G, v): 
        # 방문하지 않았으면 재귀
        if not visited[w]:
            DFS_recursive(G, w)
```

```python
# pseudo code, iterate
s = []
visited=[]
def DFS(v):
	push(s,v)
    while not isEmpty(s):
        v <- pop(s)
        if not visited[v]:	
            visit(v) 		# 방문 처리하고
            for each w in adjacency(v)  # 인접한 모든 정점에서
            	if not visited[w]		# 방문하지 않은 점들을
                	push(s, w)			# 스택에 저장
```



알고리즘 구현

```python
V, E = map(int, input().split())
G = [[] for _ in range(V + 1)] # 그래프
visit = [0] * (V + 1)          # 방문정보
S = []
for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

v = 1
# 1) 시작 정점 v를 결정하여 방문한다.
visit[v] = 1; print(v, end=' ')
S.append(v)
while S:
    # 스택이 공백이 될 때까지 2)를 반복한다.
    # 2) 정점 v에 인접한 정점 중에서 방문하지 않은 정점 w를 찾는다.
    for w in G[v]:
        if visit[w] == 0:
            S.append(v)
            # 정점 v를 스택에 push하고 정점 w를 방문한다.
            visit[w] = 1; print(w, end=' ')  
            # 그리고 w를 v로 하여 다시 2)를 반복한다.            
            v = w       
            break
    else:
        # 방문하지 않은 정점이 없으면, 
        # 탐색의 방향을 바꾸기 위해서
        # 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2)를 반복한다.
        v = S.pop()     
```

```python
# bfs 랑 비슷한 방식
v,e = map(int, input().split())
g = [[] for _ in range(v+1)] #graph
visit = [0]*(v+1) #방문정보
s = [] #stack

for _ in range(e):
    u,v = map(int,input().split())
    g[u].append(v)
    g[v].append(u)

v=1
s.append(v)
while s:
    v = s.pop()
    if not visit[v]:
        visit[v] = 1
		for w in g[v]:
            if not visit[w]:
                s.append(w)
```

```python
#재귀호출방식
def DFS(v):
    visit[v] = 1
    for w in range(g[v]):
        if not visit[w]:
            DFS(w)

v,e = map(int, input().split())
g = [[] for _ in range(v+1)] #graph
visit = [0]*(v+1) #방문정보
s = [] #stack

for _ in range(e):
    u,v = map(int,input().split())
    g[u].append(v)
    g[v].append(u)
    
DFS(1)
```

```python
# 내가 짜본건데 잘 돌아가는듯하다.
stack = [start]
while stack:
    v_node = stack[-1]
    visited[v_node] = 1
    for w in g[v_node]:
        if not visited[w]:
            stack.append(w)
            break
    else:
        stack.pop()
```





## 너비 우선탐색 Breadth First Search







