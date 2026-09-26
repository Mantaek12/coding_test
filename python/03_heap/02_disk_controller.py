import heapq

def solution(jobs):

    answer = 0

    # 처음에는 대기 큐가 비어있음 -> 채워줘야함
    # 작업 x 및 대기가 있다면 우선순위 높은 작업을 꺼내서 진행 (소요시간 짧은것 -> 요청 시각 빠른것 -> 번호 작은 것 순으로)
    # 동시 작업 불가
    # 작업 마치는 시점과 들어오는 시점이 겹치면 작업 끝나자마자 요청

    # 요청 시간 순으로 정렬함
    jobs.sort(key=lambda x:x[0])
    # print(f"요청시간 순 정렬 {jobs}")
    n = len(jobs)  # jobs.pop(0)으로 계속 줄어들기 때문에 개수는 미리 저장


    current_time = 0
    waiting = []
    request_time = 0
    working_time = 0
    i = 0

    while jobs or waiting:
        while jobs and jobs[0][0] <= current_time:

            # print(f"현재 시간 : {current_time}")
            request_time, working_time = jobs.pop(0)
            heapq.heappush(waiting, [working_time, request_time])

            
            # i +=1

        if waiting:
            working_time, request_time = heapq.heappop(waiting)
            print("꺼낸 작업:", [working_time, request_time])
            print("남은 대기 큐:", waiting)
            current_time += working_time
            answer += current_time - request_time
            
        
        else:
            current_time = jobs[0][0]
   
    return answer // n



if __name__ == "__main__":
    jobs = [[0, 3], [1, 9], [3, 5], [100, 100]]
    result = solution(jobs)

    print(result)  # Expected output: 8
