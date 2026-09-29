import heapq

def solution(scoville, K):

    answer = 0
    


    heapq.heapify(scoville)

    while True:

        new_scoville = 0

        if scoville[0] < K:
            if len(scoville) < 2:
                return -1
            else:
                first = heapq.heappop(scoville)
                second = heapq.heappop(scoville)
                new_scoville = first + second * 2
                heapq.heappush(scoville, new_scoville)
                answer +=1
                
        else:
            return answer
            


if __name__ == "__main__":
    scoville = [1, 2, 3, 9, 10, 12]	
    k = 7
    print(solution(scoville, k))