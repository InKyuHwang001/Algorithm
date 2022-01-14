# DFS/BFS
---
## 자료구조의 기초
---
- 탐색: 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
- 자료구조: 데이터를 표현하고 관리하고 처리하기 위한 구조
### 스택
- 선입후출구조
- https://github.com/InKyuHwang001/Algorithm/blob/master/3.%EC%8A%A4%ED%83%9D.md
### 큐 
- 선입후출구조
- https://github.com/InKyuHwang001/Algorithm/blob/master/5.%ED%81%90.md
### 재귀함수
- 자기 자신을 다시 호출하는 함수
- https://github.com/InKyuHwang001/Algorithm/blob/master/5.%ED%81%90.md
---
## 탐색 알고리즘 DFS/BFS
---
### DFS
- 깊이 우선 탐색이라고 
- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.(먼 것부터 탐색)
- 그래프는 노드(정점) 엣지(간선)로 구성된다
#### 인접행렬 방식
- 2차원 배열에 각 노드가 연결된 형태를 기록하는 방식이다.


```python
inf=11111
graph=[[0,7,5],[7,0,inf],[5,inf,0]]
print(graph)
```

    [[0, 7, 5], [7, 0, 11111], [5, 11111, 0]]
    

#### 인접 리스트 방식


```python
#행이 3개인 2차원 리스트 표현
graph=[[]for _ in range(3)]
#노드0 에  연결된 도드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))
graph[1].append((0,7))
graph[2].append((0,5))
print(graph)
```

    [[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]
    


```python
#DFS정의
def dfs(graph, v, visted):
    #현재노드를 방문처리
    visited[v]=True
    print(v, end='')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
#각 노드가 연결된 정보를 리스트 자료형으로 표현
graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited=[False]*9
#정의된 DFS 함수 호충
dfs(graph, 1,visited)
```

    12768345

### BFS
- 너비 우선 탐색
- 가까운 노드부터 탐색하는 알고리즘


```python
from collections import deque
#BFS 메서드 정의
def bfs(graph,start,visited):
    #큐 구현을 위한 디큐라이브러리 사용
    queue=deque([start])
    #현재 노드를 방문 처리
    visited[start]=True
    #큐가 빌 때까지 반복
    while queue:
        #큐에서 하나의 원소를 뽑아 출력
        v=queue.popleft()
        print(v,end='')
        #해당 원소와 연결된 미방문 원소를 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
#각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원)
graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
#각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원)
visited=[False]*9
#호출
bfs(graph,1,visited)
```

    12387456


```python

```
