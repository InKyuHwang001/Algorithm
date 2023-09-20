from collections import deque
def solution(tickets):
    answer = []
    q = deque()
    q.append(("ICN",["ICN"], []))
    
    while q:
        airport, path, used = q.popleft()

        if len(used) == len(tickets):
            answer.append(path)
        
        for idx, ticket in enumerate(tickets):
            if ticket[0] == airport and not idx in used:
                q.append((ticket[1], path+[ticket[1]], used+[idx]))
                
    
    answer.sort()

    return answer[0]

def solution(tickets):
    answer = []
    
    visited = [False]*len(tickets)
    
    def dfs(airport, path):
        if len(path) == len(tickets)+1:
            answer.append(path)
            return
        
        for idx, ticket in enumerate(tickets):
            if airport == ticket[0] and visited[idx] == False:
                visited[idx] = True
                dfs(ticket[1], path+[ticket[1]])
                visited[idx] = False
        
        
    dfs("ICN", ["ICN"])
    
    answer.sort()

    return answer[0]