def solution(n, computers):
    answer = 0

    visited = [False] * n

    def check_network(idx):
        visited[idx] = True

        for i in range(n):
            server = computers[idx][i]

            if server == 1 and visited[i] == False:
                check_network(i)


    for i in range(n):
        if visited[i] == False:
            answer += 1
            check_network(i)

    return answer
if __name__ == "__main__":
    n = 3
    computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(n, computers))