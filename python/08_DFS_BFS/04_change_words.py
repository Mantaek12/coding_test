from collections import deque

def solution(begin, target, words):

    visited = [False] * len(words)

    def bfs(start):
        queue = deque([(start, 0)])
        
        while queue:
            current, dis = queue.popleft()

            if current == target:
                return dis

            for i in range(len(words)):
                next_word = words[i]

                if not visited[i]:
                    diff = 0
                    n = len(next_word)
                    for j in range(n):
                        if current[j] != next_word[j]:
                            diff += 1

                    if diff == 1:
                        visited[i] = True
                        queue.append((next_word, dis+1))
                    pass



        return 0

    return bfs(begin)
                    
if __name__ == "__main__":
    begin1 = "hit"
    target1 = "cog"
    words1 = ["hot", "dot", "dog", "lot", "log", "cog"]	
    print(solution(begin1, target1, words1))

    begin2 = "hit"
    target2 = "cog"
    words2 = ["hot", "dot", "dog", "lot", "log"]
    print(solution(begin2, target2, words2))



