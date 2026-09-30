def solution(n, times):
    answer = False
    left = 1
    right = max(times)*n
    # print(right)



    while left <= right:

        mid = (left+right) // 2
        tot_people = 0

        for i in times:
            tot_people += mid // i

        if tot_people >= n :
            right = mid - 1
        elif tot_people < n:
            left = mid + 1


    return left 

if __name__ == "__main__":
    n = 6
    times = [7, 10]
    print(solution(n, times))