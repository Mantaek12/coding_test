from collections import deque

def solution(maps):

    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]

    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(start):
        queue = deque([start])
        
        x, y, _ = start
        visited[x][y] = True

        while queue:
            
            current = queue.popleft()
            
            x, y, dis = current
            
            if x == n-1 and y == m-1:
                return dis

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 맵 밖이면 넘어감
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                # 벽이면 넘어감
                if maps[nx][ny] == 0:
                    continue


                # 아직 방문하지 않았다면
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dis+1))
                    
        return -1
    
    return bfs((0, 0, 1))
                   


if __name__ == "__main__":
    maps1 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	
    print(solution(maps1))

    maps2 = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
    print(solution(maps2))


