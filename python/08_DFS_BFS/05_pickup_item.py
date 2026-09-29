from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    maps = [[0] * 102 for _ in range(102)]
    # print(maps)
    # print(rectangle[0])   
    for x1, y1, x2, y2 in rectangle:
        x1 *=2
        y1 *=2
        x2 *=2
        y2 *=2

        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                maps[y][x] = 1

    for x1, y1, x2, y2 in rectangle:

        x1 *=2
        y1 *=2
        x2 *=2
        y2 *=2

        for i in range(x1+1, x2):
            for j in range(y1+1, y2):
                maps[j][i]  = 0

    # print(maps)

    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2


    dx = [-1, 1, 0, 0]      # 좌 | 우
    dy = [0, 0, -1, 1]      # 하 | 상

    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]


    def bfs(start):
        queue = deque([start])
        # print(queue)
        x, y, dis = start
        visited[y][x] = True



        while queue:

            current = queue.popleft()
            x, y, dis = current
            if x == itemX and y == itemY:
                return dis

            for i in range(4):
                nx = x + dx[i] 
                ny = y + dy[i]

                if maps[ny][nx] == 1:
                    if not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append((nx, ny, dis + 1))




        return -1

    
    
    return bfs((characterX, characterY, 0)) // 2


if __name__ == "__main__": 
    rectangle = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]	
    characterX = 1
    characterY = 3
    itemX = 7
    itemY = 8

    print(solution(rectangle, characterX, characterY, itemX, itemY))