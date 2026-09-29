def solution(tickets):
    answer = []

    visited = [False] * len(tickets)

    tickets.sort()
    print(tickets)
    
    answer.append("ICN")
    def dfs(current):

        if len(answer) == len(tickets) + 1:
            return True

        for i in range(len(tickets)):
            start = tickets[i][0]
            end = tickets[i][1]

            if start == current and visited[i] == False:

                visited[i] = True
                answer.append(end)

                if dfs(end):
                    return True

                answer.pop()
                visited[i] = False

        return False
    
    dfs("ICN")

    return answer

if __name__ == "__main__":
    tickets1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	
    print(solution(tickets1))

    tickets2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	
    print(solution(tickets2))