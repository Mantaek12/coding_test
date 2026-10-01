from collections import Counter

def solution(k, tangerine):
    answer = 0


    cnt = Counter(tangerine)
    # print(cnt)
    cnt = sorted(cnt.values(), reverse=True)
    # print(cnt)

    for i in range(0, len(cnt)):
        # print(cnt[i])
        k -= cnt[i]
        answer +=1
        if k <= 0 :
            return answer
        else:
            pass
    
    return answer




if __name__ == "__main__":
    print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))

    print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))

    print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))
