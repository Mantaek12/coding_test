import heapq

def solution(n, works):
    answer = 0

    reverse_works = []

    if sum(works) <= n:
        return 0

    for work in works:
        heapq.heappush(reverse_works, -work)

    # print(reverse_works)
    while n !=0 :
        min_num = heapq.heappop(reverse_works)
        min_num += 1
        heapq.heappush(reverse_works, min_num) 
        n -=1

    for i in reverse_works:
        answer += i ** 2

    
    return answer

if __name__ == "__main__":
    print(solution(4, [4, 3, 3]))
    print(solution(1, [2, 1, 2]))
    print(solution(3, [1, 1]))